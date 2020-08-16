import sys, os
LIB_PATH = '../01_point_in_3d_space'
sys.path.append(LIB_PATH)
from Vector import *

class color(vec3d):
    """docstring for color."""

    def __init__(self, r, g, b):
        r = max(min(r, 255), 0)
        g = max(min(g, 255), 0)
        b = max(min(b, 255), 0)
        vec3d.__init__(self, r, g, b)

    def show(self):
        print("This color is {}".format((self.x, self.y, self.z)))

    def setR(self, r):
        self.x = r

    def getR(self):
        return self.x

    def setG(self, g):
        self.y = g

    def getG(self):
        return self.y

    def setB(self, b):
        self.z = b

    def getB(self):
        return self.z

class image(object):
    """Creat an image. width and height are in pixel"""

    def __init__(self, width, height):
        super(image, self).__init__()
        self.width = width
        self.height = height
        self.color_vec_mat = [[None for _ in range(self.width)] for _ in range(self.height)]

    def addColor(self, color_vec):
        if self.color_vec_mat[self.height-1][self.width-1] != []:
            print("Cannot add more!")
        else:
            for i in range(self.height):
                ifBreak = False
                for j in range(self.width):
                    if self.color_vec_mat[i][j] == []:
                        self.color_vec_mat[i][j] = color_vec
                        ifBreak = True
                        break
                if ifBreak:
                    break

    def setColor(self, color_vec, x, y):
        self.color_vec_mat[y][x] = color_vec

    def saveImage(self, file_name):
        with open(file_name, "w") as f:
            f.write("P3\t{}\t{}\n".format(self.width, self.height))
            f.write("255\n")
            for i in range(self.height):
                for j in range(self.width):
                    color_vec = self.color_vec_mat[i][j]
                    f.write("{}\t{}\t{}\t".format(int(color_vec.x), int(color_vec.y), int(color_vec.z)))
                f.write("\n")
            print("Done")

def main():
    import random
    random.seed(2)
    WIDTH = 4
    HEIGHT = 5
    i2 = image(WIDTH, HEIGHT)
    c = []
    for i in range(WIDTH*HEIGHT):
        c.append(color(random.randint(0, 255), random.randint(0, 255) ,random.randint(0, 255)))

    # print(c)
    for pix in c:
        i2.addColor(pix)
    i2.saveImage("result.ppm")

if __name__ == '__main__':
    main()
