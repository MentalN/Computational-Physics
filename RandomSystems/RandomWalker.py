#   File: RandomWalker.py
#   Author: Nawaf Abdullah
#   Creation Date: 19/Mar/2018
#   Description: Modeling of the random walker problem in 1D and 2D
#   Reference: Computational Physics by Nichholas J. Giordano & Hisao Nakanishi (2nd Ed)
import matplotlib.pyplot as plt
import random


class Walker:
    n_points = 0
    x = [0]
    y = [0]
    z = [0]

    def __init__(self, N):
        self.n_points = N
        for i in range(N-1):
            self.x.append(0)
            self.y.append(0)
            self.z.append(0)

    def one_dimension(self):
        for i in range(self.n_points-1):
            r = random.randint(0, 100)
            if r > 50:
                self.x[i] = self.x[i] + 1
            else:
                self.x[i] = self.x[i] - 1
            self.y[i+1] = self.y[i] + 1
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
        return self.x, self.y

    def plot_walker(self):
        fig1 = plt.figure(1)
        fig1.suptitle("Walker Path")
        plt.xlabel("x-position")
        plt.ylabel("y-position")
        plt.plot(self.x, self.y)
        plt.show()


walker1 = Walker(100)
#   walker1.one_dimension()
#   walker1.two_dimension()
walker1.plot_walker()
