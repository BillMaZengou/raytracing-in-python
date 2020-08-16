from color import *

def gradient(color_min, color_max, n_level):
    d_color = (color_max - color_min) / (n_level-1)
    color_range = [color_min+i*d_color for i in range(n_level)]
    return color_range

def main():
    WIDTH = 200
    HEIGHT = 100
    IMG = image(WIDTH, HEIGHT)
    a = color(100, 100, 255)
    b = color(200, 100, 255)
    color_range = gradient(a, b, HEIGHT)

    for j in range(HEIGHT):
        for i in range(WIDTH):
            IMG.setColor(color_range[j], i, j)
    IMG.saveImage("gradient_result.ppm")

if __name__ == '__main__':
    main()
