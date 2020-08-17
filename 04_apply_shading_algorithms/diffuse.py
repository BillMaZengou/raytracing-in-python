import sys, os
LIB_PATH = '../01_point_in_3d_space'
sys.path.append(LIB_PATH)
from Vector import *
from mathTools import sqrt
LIB_PATH = '../02_revealing_the_true_colors'
sys.path.append(LIB_PATH)
from color import *
LIB_PATH = '../03_3d_balls_in_2d_space'
sys.path.append(LIB_PATH)
from simplified_raytracing import *

class Material(object):
    """docstring for Material."""

    def __init__(self, ambient, diffusion, specular):
        super(Material, self).__init__()
        self.ambient = ambient
        self.diffusion = diffusion
        self.specular = specular

class Light(object):
    """docstring for Light."""

    def __init__(self, source, direction):
        super(Light, self).__init__()
        self.source = source
        self.direction = direction

class Ball(object):
    """docstring for Ball."""
    def __init__(self, origin, radius, col, material):
        super(Ball, self).__init__()
        self.origin = origin
        self.radius = radius
        self.col = col
        self.material = material

    def getColor(self, camera_pos, hit_point, light_direction, M=None, k=None):
        normal_vec = hit_point - self.origin
        normal_vec /= normal_vec.get_norm()
        L = light_direction  # Light ray vector from object
        V = hit_point - camera_pos  # viewing direction
        N = normal_vec  # Normal to the surface
        C = self.col  # color at that position
        R = 2*(N.dot(L))*N - L  # Reflection vector

        """Ambient Light"""
        ambient_vec = self.material.ambient*C
        """Diffusion Light: Lambertian reflectance"""
        if M == None:
            M = self.material.diffusion
        diffuse_vec = abs(L.dot(N))*M*C
        """Specular Light: Blinn-Phong reflection model"""
        if k == None:
            k = self.material.specular
        H = L + V
        H /= H.get_norm()  # half-angle between view and light direction
        specular_vec = abs(H.dot(R)**k)*C  # Phong model uses V; BP model uses H
        k_a = 1/3
        k_d = 1/2
        k_s = 1/6
        color_vec = k_a*ambient_vec + k_d*diffuse_vec + k_s*specular_vec
        color_vec.toInteger()
        return color_vec

def main():
    WIDTH = 320
    HEIGHT = 200

    AspectRatio = aspect(WIDTH, HEIGHT)
    xMax = 1
    xMin = -xMax
    yMax = xMax/AspectRatio
    yMin = -yMax

    camera_pos = vec3d(0, 0, -1)
    ball_pos = vec3d(0, 0, 0)
    ball_r = 0.5
    ball_material = Material(0.2, 0.9, 10)

    point_light = Light(vec3d(5, 5, -1/2), vec3d(-1, -1, 1).get_unit_vec())

    red = color(255, 0, 0)
    yello = color(255, 255, 0)
    green = color(0, 255, 0)

    ball1 = Ball(ball_pos, ball_r, red, ball_material)

    image_plane = Plane(ball_pos, xMin, xMax, yMin, yMax, WIDTH, HEIGHT)
    ray_tracing1 = RayTracer(camera_pos, ball1, image_plane)

    IMG = image(WIDTH, HEIGHT)
    for j in range(HEIGHT):
        for i in range(WIDTH):
            single_point = None
            ray_tracing1.ray_direction(i, j)
            ray_tracing1.sphere_to_ray()
            ray_tracing1.ray_sphere_intersection()
            ray_tracing1.hit_pos()
            single_point1 = ray_tracing1.getHit()

            if single_point1 is not None:
                single_point = single_point1

            if single_point is not None:
                if single_point == single_point1:
                    color_point = ball1.getColor(camera_pos, single_point, point_light.direction, M=None, k=None)
            else:
                color_point = color(0, 0, 0)
            IMG.setColor(color_point, i, j)
    IMG.saveImage("ball.ppm")

if __name__ == '__main__':
    main()
