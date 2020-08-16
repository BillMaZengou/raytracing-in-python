import sys, os
LIB_PATH = '../01_point_in_3d_space'
sys.path.append(LIB_PATH)
from Vector import *
from mathTools import sqrt
LIB_PATH = '../02_revealing_the_true_colors'
sys.path.append(LIB_PATH)
from color import *

WIDTH = 320
HEIGHT = 200

def aspect(width, height):
    return width/height

AspectRatio = aspect(WIDTH, HEIGHT)
xMax = 1
xMin = -xMax
yMax = xMax/AspectRatio
yMin = -yMax

camera_pos = vec3d(0, 0, -1)
ball_pos = vec3d(0, 0, 0)
ball_r = 0.5
ball_col = color(255, 0, 0)

class Ball(object):
    """docstring for Ball."""

    def __init__(self, origin, radius, col):
        super(Ball, self).__init__()
        self.origin = origin
        self.radius = radius
        self.col = col

ball1 = Ball(ball_pos, ball_r, ball_col)

def sphere_to_ray(ray, sphere_origin):
    return ray - sphere_origin

ball_to_camera = sphere_to_ray(camera_pos, ball1.origin)
# print(ball_to_camera)

def ray_sphere_intersection(ray, sphere):
    # print(sphere.origin)
    # print(ray)
    ball_to_camera = sphere_to_ray(ray, sphere.origin)
    # print(ray.get_unit_vec().show())
    # print(ball_to_camera.show())
    a = 1
    b = 2 * ray.get_unit_vec().dot(ball_to_camera)
    c = ball_to_camera.dot(ball_to_camera) - sphere.radius**2
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        dist = (-b - sqrt(discriminant)) / (2*a)
        return dist
    else:
        print("There is no intersection")

distance = ray_sphere_intersection(camera_pos, ball1)

def hit_pos(ray, dist):
    return ray.origin + ray.get_unit_vec()*dist
