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
LIB_PATH = '../04_apply_shading_algorithms'
sys.path.append(LIB_PATH)
from diffuse import *
from specular import *

def main():
    """Image Plane"""
    WIDTH = 320
    HEIGHT = 200
    xMax = 1
    image_centre = vec3d(0, 0, -1/4)
    image_plane = ImagePlane(image_centre, xMax, WIDTH, HEIGHT)
    image_plane = image_plane.create_an_image_plane()

    """Camera"""
    camera_pos = vec3d(0, 0, -1)
    camera = Camera(camera_pos)

    """Colours"""
    red = color(255, 0, 0)
    yello = color(50, 50, 0)
    green = color(0, 255, 0)
    blue = color(0, 0, 255)

    """Objects"""
    balls = []
    ball_r = 0.6
    ball_material = Material(1, 0, 0)
    blue_ball = Ball(vec3d(0.25, 0.1, 1), ball_r, blue, ball_material)
    # pink_ball = Ball(vec3d(-0.75, 0.1, 2.25), ball_r, red, ball_material)
    # ground = Ball(vec3d(0, -10002, 1), 10000.0, yello, ball_material)
    balls.append(blue_ball)
    # balls.append(pink_ball)
    # balls.append(ground)

    """Lights"""
    lightSource1 = vec3d(5, 5, -3)
    lightDirection1 = vec3d(1.5, -0.5, -10.0).get_unit_vec()
    # point_light1 = Light(lightSource, lightDirection)
    lightSource2 = vec3d(5, 5, -3)
    lightDirection2 = vec3d(-0.5, -10.5, 0.0).get_unit_vec()
    # point_light2 = Light(lightSource, lightDirection)
    total_light = Light((lightSource1+lightSource2), (lightDirection1+lightDirection2))

    """Set Up Stage"""
    IMG = image(WIDTH, HEIGHT)
    stage = Stage(balls, camera, image_plane, total_light)
    stage.rayTracing()
    stage.obtain_depth()
    stage.rendering(IMG)
    IMG.saveImage("standard.ppm")

if __name__ == '__main__':
    main()
