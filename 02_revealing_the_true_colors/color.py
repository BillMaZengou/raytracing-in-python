import sys, os
LIB_PATH = '../01_point_in_3d_space'
sys.path.append(LIB_PATH)
from Vector import *

class color(vec3d):
    """docstring for color."""

    def __init__(self, r, g, b):
        if r > 255:
            r = 255
        elif r < 0:
            r = 0

        if g > 255:
            g = 255
        elif g < 0:
            g = 0

        if b > 255:
            b = 255
        elif b < 0:
            b = 0
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
        self.color_vec_mat = []
        for i in range(self.height):
            self.color_vec_mat.append([])
            for j in range(self.width):
                self.color_vec_mat[i].append([])

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

    def saveImage(self):
        with open("result.ppm", "w") as f:
            f.write("P3\t{}\t{}\n".format(self.width, self.height))
            f.write("255\n")
            for i in range(self.height):
                for j in range(self.width):
                    color_vec = self.color_vec_mat[i][j]
                    f.write("{}\t{}\t{}\t".format(color_vec.x, color_vec.y, color_vec.z))
                f.write("\n")
            print("Done")

def main():
    import random
    random.seed(2)
    i2 = image(4, 5)
    c = []
    for i in range(20):
        c.append(color(random.randint(0, 255), random.randint(0, 255) ,random.randint(0, 255)))

    # print(c)
    for pix in c:
        i2.addColor(pix)
    i2.saveImage()

if __name__ == '__main__':
    main()
