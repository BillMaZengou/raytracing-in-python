from mathTools import *

class vec3d(object):
    """x, y, z to give a 3d vector"""

    def __init__(self, x, y, z):
        super(vec3d, self).__init__()
        self.x = x
        self.y = y
        self.z = z

        self.magnitude = sqrt(x**2 + y**2 + z**2)

    def show(self):
        print("The vector is {}".format((self.x, self.y, self.z)))

    def get_norm(self):
        return self.magnitude

    def get_unit_vec(self):
        direction = vec3d(self.x/self.magnitude, self.y/self.magnitude, self.z/self.magnitude)
        return direction

    def dot(self, other_vec):
        return self.x*other_vec.x + self.y*other_vec.y + self.z*other_vec.z

    def cross(self, other_vec):
        x = self.y*other_vec.z - self.z*other_vec.y
        y = self.z*other_vec.x - self.x*other_vec.z
        z = self.x*other_vec.y - self.y*other_vec.x
        return vec3d(x, y, z)

    def __add__(self, other_vec):
        x = self.x + other_vec.x
        y = self.y + other_vec.y
        z = self.z + other_vec.z
        return vec3d(x, y, z)

    def __sub__(self, other_vec):
        x = self.x - other_vec.x
        y = self.y - other_vec.y
        z = self.z - other_vec.z
        return vec3d(x, y, z)

    def __mul__(self, factor):
        assert not isinstance(factor, vec3d)
        return vec3d(self.x*factor, self.y*factor, self.z*factor)

    def __rmul__(self, factor):
        return self.__mul__(factor)

    def __truediv__(self, factor):
        assert not isinstance(factor, vec3d)
        return vec3d(self.x/factor, self.y/factor, self.z/factor)

def main():
    v1 = vec3d(1, 2, 1)
    v2 = vec3d(1, 1, 0)
    print(v2.get_norm())
    v2.get_unit_vec().show()
    print(v1.dot(v2))
    v1.cross(v2).show()
    v1.__add__(v2).show()
    (v1 + v2).show()
    (v1 - v2).show()
    (v1*2).show()
    (v1/2).show()

if __name__ == '__main__':
    main()
