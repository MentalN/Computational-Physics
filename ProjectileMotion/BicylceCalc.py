#   File: BicycleCalc.py
#   Author: Nawaf Abdullah
#   Creation Date: 2/Feb/2018
#   Description: calculates velocity and time for a bicylce example given power,
#                mass, time step, and total number of steps.
import matplotlib.pyplot as plt

# Parameters Definitions:
# P   = Power
# m   = Mass
# dt  = Time step
# N   = number of time steps
# vo  = Initial velocity
# C   = Drag coefficient
# rho = Density of air
# A   = Frontal surface area


class Bicycle:
    v = []
    t = [0]
    cap = 0

#   Calculates the velocity of a Bicycle vs Time with no drag
    def bicycle_no_drag(self, P, m, dt, N, vo):
        self.v = [vo]
        for i in range(N):
            self.v.append(self.v[i] + (P/(m*self.v[i]))*dt)
            self.t.append(self.t[i] + dt)
        self.cap = "Bicycle Velocity vs Time (No drag)"
#       returning time array, velocity array, and a string for the plot title
        return self.t, self.v


#   Calculates the velocity of a Bicycle vs Time with drag
    def bicycle_drag(self, P, m, dt, N, vo, C, rho, A):
        self.v = [vo]
        for i in range(N):
            D = (C*rho*A*self.v[i]*self.v[i]/(2*m))*dt
            self.v.append(self.v[i] + (P/(m*self.v[i]))*dt - D)
            self.t.append(self.t[i] + dt)
            self.cap = "Bicycle Velocity vs Time (with drag)"
#       returning time array, velocity array, and a string for the plot title
        return self.t, self.v


#   Plots whatever velocity and time arrays passed to it
    def bicycle_plot(self):
        fig = plt.figure()
        fig.suptitle(self.cap)
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')
        plt.plot(self.t, self.v)
        plt.show()

