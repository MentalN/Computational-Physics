#   File: RandomWalker.py
#   Author: Nawaf Abdullah
#   Creation Date: 19/Mar/2018
#   Description: Modeling of the random walker problem in 1D, 2D and 3D
#   Reference: Computational Physics by Nichholas J. Giordano & Hisao Nakanishi (2nd Ed)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


class Walker:
    n_points = 0
    x = [0]
    y = [0]
    z = [0]
    z_switch = False

    def __init__(self, N):
        self.n_points = N
        for i in range(N-1):
            self.x.append(0)
            self.y.append(0)
            self.z.append(0)

    def init_npoints(self, N):
        del self.x[:]
        del self.y[:]
        del self.z[:]
        self.__init__(N)

    def one_dimension(self):
        for i in range(self.n_points-1):
            r = random.randint(0, 100)
            if r > 50:
                self.x[i] = self.x[i] + 1
            else:
                self.x[i] = self.x[i] - 1
            self.y[i+1] = self.y[i] + 1
        self.z_switch = False
        return self.x, self.y

    def two_dimension(self):
        for i in range(self.n_points-1):
            if i == 0:
                continue
            r = random.randint(0, 100)
            if r <= 25:
                self.x[i+1] = self.x[i] + 1
                self.y[i+1] = self.y[i]
            elif 25 < r <= 50:
                self.x[i+1] = self.x[i] - 1
                self.y[i+1] = self.y[i]
            elif 50 < r <= 75:
                self.y[i+1] = self.y[i] + 1
                self.x[i+1] = self.x[i]
            else:
                self.y[i+1] = self.y[i] - 1
                self.x[i+1] = self.x[i]
        self.z_switch = False
        return self.x, self.y

    def three_dimension(self):
        for i in range(self.n_points-1):
            if i == 0:
                continue
            r = random.randint(0, 100)
            if r <= 16.66:
                self.x[i+1] = self.x[i] + 1
                self.y[i+1] = self.y[i]
                self.z[i+1] = self.z[i]
            elif 16.66 < r <= 33.32:
                self.x[i+1] = self.x[i] - 1
                self.y[i+1] = self.y[i]
                self.z[i+1] = self.z[i]
            elif 33.32 < r <= 49.98:
                self.y[i+1] = self.y[i] + 1
                self.x[i+1] = self.x[i]
                self.z[i+1] = self.z[i]
            elif 49.98 < r <= 66.64:
                self.y[i+1] = self.y[i] - 1
                self.x[i+1] = self.x[i]
                self.z[i+1] = self.z[i]
            elif 66.64 < r < 83.33:
                self.z[i+1] = self.z[i] + 1
                self.x[i+1] = self.x[i]
                self.y[i+1] = self.y[i]
            else:
                self.z[i+1] = self.z[i] - 1
                self.x[i+1] = self.x[i]
                self.y[i+1] = self.y[i]
        self.z_switch = True
        return self.x, self.y, self.z

    def plot_walker(self):
        if self.z_switch is True:
            ax = plt.axes(projection='3d')
            ax.plot3D(self.x, self.y, self.z, 'gray')
            plt.show()
        else:
            fig1 = plt.figure(1)
            fig1.suptitle("Walker Path")
            plt.xlabel("x-position")
            plt.ylabel("y-position")
            plt.plot(self.x, self.y)
            plt.show()
