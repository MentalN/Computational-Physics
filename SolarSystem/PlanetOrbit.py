#   File: PlanetOrbit.py
#   Author: Nawaf Abdullah
#   Creation Date: 18/Mar/2018
#   Description: plots the orbit of a planet
#   Reference: Simulation of Earth orbit around Sun by Computational Method.
#              Kumar, Pramod. et al.
import matplotlib.pyplot as plt
from math import sqrt

#   Parameters Definitions:
#   N     = number of time step points
#   dt    = time step in years
#   vx_i  = initial velocity x-component(AU/year)
#   vy_i  = initial velocity y-component(AU/year)
#   x_i   = initial x-location (AU)
#   y_i   = initial y-location (AU)
Pi = 3.14159


class Planet:
    x = []
    y = []

    def planet_position(self, x_i, y_i, vx_i, vy_i, N, dt):
        self.x = [x_i]
        self.y = [y_i]
        vx = [vx_i]
        vy = [vy_i]
        for i in range(N-1):
            r = sqrt(self.x[i]**2 + self.y[i]**2)
            vx.append(vx[i]-((4*Pi*Pi*self.x[i]*dt)/(r**3)))
            vy.append(vy[i]-((4*Pi*Pi*self.y[i]*dt)/(r**3)))
            self.x.append(self.x[i]+vx[i+1]*dt)
            self.y.append(self.y[i]+vy[i+1]*dt)
        return self.x, self.y

    def planet_plot(self):
        fig1 = plt.figure(1)
        fig1.suptitle("Planet Motion")
        plt.xlabel("x-position (AU)")
        plt.ylabel("y-position (AU)")
        plt.plot(self.x, self.y)
        plt.show()


