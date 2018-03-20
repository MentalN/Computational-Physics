#   File: RandomWalker.py
#   Author: Nawaf Abdullah
#   Creation Date: 19/Mar/2018
#   Description: Modeling of the random walker problem in 1D and 2D
#   Reference: Computational Physics by Nichholas J. Giordano & Hisao Nakanishi (2nd Ed)
import matplotlib.pyplot as plt
import random


class Walker:
    x = [0]
    y = [0]
    z = [0]

    def one_dimension(self, N):
        for i in range(N):
            r = random.randint(0, 100)
            if r > 50:
                self.x.append(self.x[i]+1)
            else:
                self.x.append(self.x[i]-1)
            self.y.append(self.y[i]+1)
        return self.x, self.y

    def plot_walker(self):
        fig1 = plt.figure(1)
        fig1.suptitle("Walker Path")
        plt.xlabel("x-position")
        plt.ylabel("y-position")
        plt.plot(self.x, self.y)
        plt.show()


walker1 = Walker()
walker1.one_dimension(1000)
walker1.plot_walker()
