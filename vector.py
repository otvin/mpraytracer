import math
import random


NEAR_ZERO = 0.00000001


class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __iadd__(self, other):
        # assert isinstance(other, Vector3)
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

    def __idiv__(self, scalar):
        return self.__imul__(1.0/scalar)

    def __str__(self):
        return '{} {} {}'.format(self.x, self.y, self.z)

    def __add__(self, other):
        # assert isinstance(other, Vector3)
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        # assert isinstance(other, Vector3)
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        return self.__mul__(1.0/other)

    def length_squared(self):
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)

    def length(self):
        return math.sqrt(self.length_squared())

    def near_zero(self):
        # returns true if the vector is close to zero in all dimensions
        return math.fabs(self.x) < NEAR_ZERO and math.fabs(self.y) < NEAR_ZERO and math.fabs(self.z) < NEAR_ZERO


def random_vector():
    return Vector3(random.random(), random.random(), random.random())


def random_vector_range(rangemin, rangemax):
    return Vector3(random.uniform(rangemin, rangemax), random.uniform(rangemin, rangemax),
                   random.uniform(rangemin, rangemax))


def random_unit_vector():
    return unit_vector(random_vector())


def random_in_unit_disk():
    done = False
    p = None
    while not done:
        p = Vector3(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), 0.0)
        if p.length_squared() < 1:
            done = True
    return p

def dot(u, v):
    # assert isinstance(u, Vector3)
    # assert isinstance(v, Vector3)
    return (u.x * v.x) + (u.y * v.y) + (u.z * v.z)


def cross(u, v):
    # assert isinstance(u, Vector3)
    # assert isinstance(v, Vector3)
    return Vector3(u.y * v.z - u.z * v.y,
                   u.z * v.x - u.x * v.z,
                   u.x * v.y - u.y * v.x)


def unit_vector(v):
    # assert isinstance(v, Vector3)
    return v / v.length()

# point is just an alias for vector
class Point3(Vector3):
    pass


class Color(Vector3):
    pass


class Ray:
    def __init__(self, origin=Point3(), direction=Vector3()):
        # assert isinstance(origin, Vector3)
        # assert isinstance(direction, Vector3)
        # if we get weird things later on, make origin and direction copies of the parameters
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return self.origin + (self.direction * t)
