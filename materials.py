from vector import *


def reflect(v, n):
    # reflects v across the normal vector n
    # assert isinstance(v, Vector3)
    # assert isinstance(n, Vector3)
    return v - (n * (dot(v, n) * 2))


def reflectance(cosine, refraction_index):
    # Schlick's approximation for reflectance.  Glass that is see-through at most angles but becomes
    # mirror at steep angles.
    r0 = (1.0-refraction_index) / (1.0+refraction_index)
    r0 = r0 * r0
    return r0 + (1-r0) * math.pow((1-cosine), 5)


def refract(uv, n, eta_over_eta_prime):
    # eta_over_eta_prime is the ratio of refractive indices.  Air = 1.0,
    # glass = 1.3-1.7, diamond = 2.4.  uv is the vector and n is the normal
    # across which the refraction occurs.  (Snell's law)
    # assert isinstance(uv, Vector3)
    # assert isinstance(n, Vector3)
    cos_theta = min(dot(-uv, n), 1.0)
    r_out_perpendicular = (uv + (n * cos_theta)) * eta_over_eta_prime
    r_out_parallel = n * (-math.sqrt(math.fabs(1.0 - r_out_perpendicular.length_squared())))
    return r_out_perpendicular + r_out_parallel


class Material:
    def __init__(self):
        pass

    def scatter(self, r_in, rec):
        # returns true/false if the ray is scattered (true) or absorbed (false).
        # if scattered, then an attentuation (color) and a ray showing the direction.
        return False, Color(0, 0, 0), Ray(Point3(0, 0, 0), Vector3(0, 0, 0))


class Lambertian(Material):
    def __init__(self, albedo=Color(0, 0, 0)):
        # assert isinstance(albedo, Vector3)
        super().__init__()
        self.albedo = albedo

    def scatter(self, r_in, rec):
        # assert isinstance(r_in, Ray)
        # assert isinstance(rec, HitRecord)
        scatter_direction = rec.normal + random_unit_vector()
        # catch degenerate scatter condition where random vector == the opposite of the normal
        if scatter_direction.near_zero():
            scatter_direction = rec.normal
        return True, self.albedo, Ray(rec.p, scatter_direction)


class Metal(Material):
    def __init__(self, albedo=Color(0, 0, 0), fuzz=0.0):
        # assert isinstance(albedo, Vector3)
        # assert 0.0 <= fuzz <= 1.0
        super().__init__()
        self.albedo = albedo
        self.fuzz = fuzz

    def scatter(self, r_in, rec):
        # assert isinstance(r_in, Ray)
        # assert isinstance(rec, HitRecord)
        reflected = reflect(unit_vector(r_in.direction), rec.normal)
        scattered = Ray(rec.p, reflected + (random_unit_vector() * self.fuzz))
        return dot(scattered.direction, rec.normal) > 0, self.albedo, scattered


class Dielectric(Material):
    def __init__(self, index_of_refraction=1.0):
        super().__init__()
        self.albedo = Color(1.0, 1.0, 1.0)  # I have a feeling we should make this different for colored glass
        self.index_of_refraction = index_of_refraction

    def scatter(self, r_in, rec):
        # assert isinstance(r_in, Ray)
        # assert isinstance(rec, HitRecord)
        if rec.frontface:
            refraction_ratio = 1.0/self.index_of_refraction
        else:
            refraction_ratio = self.index_of_refraction

        unit_direction = unit_vector(r_in.direction)
        cos_theta = min(dot(-unit_direction, rec.normal), 1.0)
        sin_theta = math.sqrt(1.0 - (cos_theta * cos_theta))
        cannot_refract = (refraction_ratio * sin_theta) > 1.0  # must reflect in this instance

        if cannot_refract or reflectance(cos_theta, refraction_ratio) > random.random():
            direction = reflect(unit_direction, rec.normal)
        else:
            direction = refract(unit_direction, rec.normal, refraction_ratio)

        return True, self.albedo, Ray(rec.p, direction)
