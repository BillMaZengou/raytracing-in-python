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

    def getColor(self, hit_point):
        return self.col

class Plane(object):
    """docstring for Plane."""
    def __init__(self, centre, x_min, x_max, y_min, y_max, width, height):
        super(Plane, self).__init__()
        self.centre = centre
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.width = width
        self.height = height

        self.x_inc = (self.x_max - self.x_min) / self.width
        self.y_inc = (self.y_max - self.y_min) / self.height


class RayTracer(object):
    def __init__(self, camera_position, target_object, view_plane):
        super(RayTracer, self).__init__()
        self.camera = camera_position
        self.hit_target = target_object
        self.view_plane = view_plane

        self.target_to_camera = None
        self.dist = None
        self.ray = None
        self.hit = None

    def ray_direction(self, n_x, n_y):
        x_pos = self.view_plane.x_min + (n_x+1/2)*self.view_plane.x_inc
        y_pos = self.view_plane.y_max - (n_y+1/2)*self.view_plane.y_inc
        plane_aim_point = vec3d(x_pos, y_pos, self.view_plane.centre.z)
        self.ray = plane_aim_point - self.camera

    def sphere_to_ray(self):
        self.target_to_camera = self.camera - self.hit_target.origin

    def ray_sphere_intersection(self):
        a = 1
        b = 2 * self.ray.get_unit_vec().dot(self.target_to_camera)
        c = self.target_to_camera.dot(self.target_to_camera) - self.hit_target.radius**2
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            self.dist = (-b - sqrt(discriminant)) / (2*a)
        else:
            self.dist = None

    def hit_pos(self):
        if self.dist is not None:
            self.hit = self.camera + self.ray.get_unit_vec()*self.dist
        else:
            self.hit = None

    def getHit(self):
        return self.hit

ball1 = Ball(ball_pos, ball_r, ball_col)
image_plane = Plane(ball1.origin, xMin, xMax, yMin, yMax, WIDTH, HEIGHT)
ray_tracing = RayTracer(camera_pos, ball1, image_plane)
# ray_tracing.camera.show()
# ray_tracing.view_plane.centre.show()
# ray_tracing.ray_direction(0, 0)
# ray_tracing.ray_direction(160, 100)
# ray_tracing.ray.show()
# ray_tracing.sphere_to_ray()
# # ray_tracing.target_to_camera.show()
# ray_tracing.ray_sphere_intersection()
# print(ray_tracing.dist)
# position = ray_tracing.hit_pos()
# position.show()

IMG = image(WIDTH, HEIGHT)
for j in range(HEIGHT):
    for i in range(WIDTH):
        ray_tracing.ray_direction(i, j)
        ray_tracing.sphere_to_ray()
        ray_tracing.ray_sphere_intersection()
        ray_tracing.hit_pos()
        single_point = ray_tracing.getHit()
        if single_point is not None:
            color_point = ball1.getColor(single_point)
        else:
            color_point = color(0, 0, 0)
        IMG.setColor(color_point, i, j)

IMG.saveImage("ball.ppm")
