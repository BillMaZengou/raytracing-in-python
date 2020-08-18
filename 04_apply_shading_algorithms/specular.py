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
from diffuse import *

class Stage(object):
    """docstring for Stage."""

    def __init__(self, objects, camera, image_plane, lights):
        super(Stage, self).__init__()
        self.objects = objects
        self.camera = camera
        self.image_plane = image_plane
        self.lights = lights

        self.ray_tracer = None
        self.z_buffer = None

    def rayTracing(self):
        self.ray_tracer = []
        for item in self.objects:
            self.ray_tracer.append(RayTracer(self.camera.getPos(), item, self.image_plane))

    def obtain_depth(self):
        """Use previously made 'image' function to do a depth buffer"""
        self.z_buffer = image(self.image_plane.width, self.image_plane.height)
        for j in range(self.image_plane.height):
            for i in range(self.image_plane.width):
                single_point = None
                for ray_tracing in self.ray_tracer:
                    ray_tracing.ray_direction(i, j)
                    ray_tracing.sphere_to_ray()
                    ray_tracing.ray_sphere_intersection()
                    ray_tracing.hit_pos()
                    hit_point = ray_tracing.getHit()

                if single_point is None:
                    single_point = hit_point
                elif single_point is not None and single_point.z > hit_point.z:
                    single_point = hit_point
                self.z_buffer.setColor(single_point, i, j)

    def rendering(self, final_image):
        for j in range(final_image.height):
            for i in range(final_image.width):
                color_point = color(0, 0, 0)
                local_depth = self.z_buffer.getValue(i, j)
                for k in range(len(self.ray_tracer)):
                    self.ray_tracer[k].ray_direction(i, j)
                    self.ray_tracer[k].sphere_to_ray()
                    self.ray_tracer[k].ray_sphere_intersection()
                    self.ray_tracer[k].hit_pos()
                    hit_point = self.ray_tracer[k].getHit()
                    if local_depth is not None and hit_point is not None:
                        if hit_point.z == local_depth.z:
                            color_point = self.objects[k].getColor(self.camera.getPos(), hit_point, self.lights.direction, k_a=(1/12), k_d=(1/3), k_s=(7/12))
                    else:
                        color_point = color(0, 0, 0)
                final_image.setColor(color_point, i, j)

class ImagePlane(object):
    """docstring for Image_Plane."""

    def __init__(self, centre, x_max, width, height):
        super(ImagePlane, self).__init__()
        self.centre = centre
        self.x_max = x_max
        self.width = width
        self.height = height

        self.aspect_ratio = aspect(self.width, self.height)
        self.x_min = -self.x_max
        self.y_max = self.x_max / self.aspect_ratio
        self.y_min = -self.y_max

    def create_an_image_plane(self):
        return Plane(self.centre, self.x_min, self.x_max, self.y_min, self.y_max, self.width, self.height)

class Camera(object):
    """docstring for Camera."""

    def __init__(self, camera_position):
        super(Camera, self).__init__()
        self.camera_position = camera_position

    def getPos(self):
        return self.camera_position


def main():
    """Image Plane"""
    WIDTH = 320
    HEIGHT = 200
    xMax = 1
    image_centre = vec3d(0, 0, 0)
    image_plane = ImagePlane(image_centre, xMax, WIDTH, HEIGHT)
    image_plane = image_plane.create_an_image_plane()

    """Camera"""
    camera_pos = vec3d(0, 0, -1)
    camera = Camera(camera_pos)

    """Colours"""
    red = color(255, 0, 0)
    yello = color(255, 255, 0)
    green = color(0, 255, 0)

    """Objects"""
    ball_pos = vec3d(0, 0, 0)
    ball_r = 0.5
    ball_material = Material(0.3, 0.9, 5)
    ball1 = Ball(ball_pos, ball_r, red, ball_material)
    balls = [ball1]

    """Lights"""
    lightSource = vec3d(5, 5, -3)
    lightDirection = vec3d(1, 1, -1).get_unit_vec()
    point_light = Light(lightSource, lightDirection)

    """Set Up Stage"""
    IMG = image(WIDTH, HEIGHT)
    stage = Stage(balls, camera, image_plane, point_light)
    stage.rayTracing()
    stage.obtain_depth()
    stage.rendering(IMG)
    IMG.saveImage("ball2.ppm")

if __name__ == '__main__':
    main()
