# modeled after https://raytracing.github.io/books/RayTracingInOneWeekend.html
import multiprocessing as mp
import time
from scenes import *


def clamp(x, minimum, maximum):
    if x < minimum:
        return minimum
    if x > maximum:
        return maximum
    return x


def write_file(filename, gp, image_width, image_height, samples_per_pixel, maxcolors):
    f = open(filename, "w")
    f.write("P3\n")
    f.write("{} {}\n".format(image_width, image_height))
    f.write("255\n")
    scale = 1.0 / samples_per_pixel
    for h in range(image_height - 1, -1, -1):
        for w in range(image_width):
            r = gp[(h * image_width * 3) + (3 * w)]
            g = gp[(h * image_width * 3) + (3 * w) + 1]
            b = gp[(h * image_width * 3) + (3 * w) + 2]
            r = math.sqrt(scale * r)
            g = math.sqrt(scale * g)
            b = math.sqrt(scale * b)
            r = int((maxcolors + 1) * clamp(r, 0.0, 0.999))
            g = int((maxcolors + 1) * clamp(g, 0.0, 0.999))
            b = int((maxcolors + 1) * clamp(b, 0.0, 0.999))
            f.write('{} {} {}\n'.format(r, g, b))
    f.close()


class Camera:
    def __init__(self, lookfrom, lookat, vup, vfov, aspect_ratio, aperture, focus_dist):
        # vup = view up vector
        # vfov = vertical field of view in degrees.
        # assert isinstance(lookfrom, Point3)
        # assert isinstance(lookat, Point3)
        # assert isinstance(vup, Vector3)

        self.aspect_ratio = aspect_ratio
        self.vfov = vfov
        theta = math.radians(self.vfov)
        h = math.tan(theta/2.0)
        self.viewport_height = 2.0 * h
        self.viewport_width = aspect_ratio * self.viewport_height
        self.aperture = aperture
        self.focus_dist = focus_dist

        self.w = unit_vector(lookfrom - lookat)
        self.u = unit_vector(cross(vup, self.w))
        self.v = cross(self.w, self.u)

        self.origin = lookfrom
        self.horizontal = self.u * self.viewport_width * self.focus_dist
        self.vertical = self.v * self.viewport_height * self.focus_dist
        self.lower_left_corner = self.origin - (self.horizontal/2) - (self.vertical/2) - (self.w * focus_dist)
        self.lens_radius = self.aperture/2.0

    def get_ray(self, s, t):
        rd = random_in_unit_disk() * self.lens_radius
        offset = (self.u * rd.x) + (self.v * rd.y)

        return Ray(self.origin + offset,
                   self.lower_left_corner + (self.horizontal * s) + (self.vertical * t) - self.origin - offset)


def ray_color(r, depth):
    # assert isinstance(r, Ray)
    # assert isinstance(GLOBALWORLD, Scene)
    global GLOBALWORLD

    # If we've exceeded the ray bounce limit, no more light is gathered
    if depth <= 0:
        return Color(0, 0, 0)

    didhit, hitrec = GLOBALWORLD.hit(r, 0.001, math.inf)
    if didhit:
        didscatter, attenuation, scat_direction = hitrec.material.scatter(r, hitrec)
        if didscatter:
            return attenuation * ray_color(scat_direction, depth-1)
        else:
            return Color(0, 0, 0)
    else:
        unit_direction = unit_vector(r.direction)
        # this is to print a pretty gradient.  unit_direction.y is a number between 0 and 1.
        t = 0.5 * (unit_direction.y + 1.0)
        r = (1.0 - t) + (0.5 * t)
        g = (1.0 - t) + (0.7 * t)
        b = (1.0 - t) + t
        return Color(r, g, b)


setup_globalworld()

GLOBAL_ASPECTRATIO = 3.0 / 2.0
lookfrom = Point3(13.0, 2.0, 3.0)
lookat = Point3(0.0, 0.0, 0.0)
vup = Vector3(0.0, 1.0, 0.0)
dist_to_focus = 10.0
aperture = 0.1

GLOBALCAMERA = Camera(lookfrom, lookat, vup, 20, GLOBAL_ASPECTRATIO, aperture, dist_to_focus)

def render_rows(gp, rowlist, image_width, image_height, samples_per_pixel, max_depth):
    global GLOBALCAMERA

    for h in rowlist:
        for w in range(image_width):
            pixel_color = Color(0.0, 0.0, 0.0)
            for sample in range(samples_per_pixel):
                u = (w + random.random()) / (image_width - 1.0)
                v = (h + random.random()) / (image_height - 1.0)
                r = GLOBALCAMERA.get_ray(u, v)
                pixel_color += ray_color(r, max_depth)
            gp[(h * image_width * 3) + (3 * w)] = pixel_color.x
            gp[(h * image_width * 3) + (3 * w) + 1] = pixel_color.y
            gp[(h * image_width * 3) + (3 * w) + 2] = pixel_color.z
        print('line {} completed.'.format(h), flush=True)


def render():
    global GLOBALCAMERA
    global GLOBAL_ASPECTRATIO

    image_width = 800
    image_height = int(image_width / GLOBAL_ASPECTRATIO)
    samples_per_pixel = 5
    max_depth = 5
    num_processes = 6

    gp = mp.Array('d', image_width * image_height * 3)

    timestart = time.time()

    rowlists = []
    for i in range(num_processes):
        rowlists.append([])

    for i in range(image_height):
        rowlists[i % num_processes].append(i)

    procArr = []
    for s in rowlists:
        p = mp.Process(target=render_rows, args = (gp, s, image_width, image_height, samples_per_pixel, max_depth))
        procArr.append(p)

    for p in procArr:
        p.start()

    for p in procArr:
        p.join()

    write_file('mpfinal2.ppm', gp, image_width, image_height, samples_per_pixel, 255)

    timeend = time.time()
    print('Elapsed time: {} seconds'.format(timeend-timestart))


if __name__ == '__main__':
    render()
