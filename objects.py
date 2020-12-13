from materials import *


class HitRecord:
    def __init__(self, p=Point3(), t=0.0):
        # assert isinstance(p, Vector3)  # should be a point, but a Point is just a vector
        self.p = p
        self.normal = None
        self.t = t
        self.frontface = True
        self.material = None

    def set_face_normal(self, r, outwardnormal):
        # assert isinstance(r, Ray)
        # assert isinstance(outwardnormal, Vector3)
        self.frontface = dot(r.direction, outwardnormal) < 0
        if self.frontface:
            self.normal = outwardnormal
        else:
            self.normal = -outwardnormal


class HittableObject:
    def __init__(self, material=Material()):
        # assert isinstance(material, Material)
        self.material = material

    def hit(self, r, t_min, t_max):
        # returns a tuple of true/false if the object is hit and then (if hit) a HitRecord
        # assert isinstance(r, Ray)
        return False, None


class Sphere(HittableObject):
    def __init__(self, center=Point3(), radius=1.0, material=Material()):
        # assert isinstance(center, Point3)
        super().__init__(material)
        self.center = center
        self.radius = radius

    def hit(self, r, t_min, t_max):
        # returns a tuple - true/false if the object is hit, and then (if hit) a HitRecord

        # assert isinstance(r, Ray)
        # Note - I did not make the changes in Listing 13 - revisit if we change the hit_sphere
        # looks like he made changes to remove two multiplications and I don't think it's worth
        # that little bit of performance since we're in Python which is slower than C++.

        # oc = r.origin - self.center
        # a = dot(r.direction, r.direction)
        # b = 2.0 * dot(oc, r.direction)
        # c = dot(oc, oc) - (self.radius * self.radius)
        # discriminant = (b * b) - (4 * a * c)

        # for performance reasons I am now making the changes in Listing 13
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = dot(oc, r.direction)
        c = oc.length_squared() - (self.radius * self.radius)
        discriminant = (half_b * half_b) - (a * c)

        if discriminant < 0:
            return False, None

        sqrtd = math.sqrt(discriminant)
        # Find the nearest root (to the camera) that lies in the acceptable range
        root = (-half_b - sqrtd) / a
        if root < t_min or root > t_max:
            root = (-half_b + sqrtd) / a
            if root < t_min or root > t_max:
                return False, None

        r_atroot = r.at(root)
        rec = HitRecord(r_atroot, root)
        outwardnormal = (r_atroot - self.center) / self.radius
        rec.set_face_normal(r, outwardnormal)
        rec.material = self.material

        return True, rec


class Scene:
    # a scene is a list of objects that can ben hit
    def __init__(self):
        self.hittablelist = []

    def clear(self):
        self.hittablelist = []

    def add(self, obj):
        # assert isinstance(obj, HittableObject)
        self.hittablelist.append(obj)

    def hit(self, r, t_min, t_max):
        # assert isinstance(r, Ray)
        returnrec = None
        hit_anything = False
        closest_so_far = t_max
        for i in self.hittablelist:
            # assert isinstance(i, HittableObject)
            h = i.hit(r, t_min, closest_so_far)
            if h[0]:
                hit_anything = True
                returnrec = h[1]
                # assert isinstance(returnrec, HitRecord)
                closest_so_far = returnrec.t

        return hit_anything, returnrec
