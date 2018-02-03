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


#   Calculates the velocity of a Bicycle vs Time with no drag
def bicycle_calc_no_drag(P, m, dt, N, vo):
    v = [vo]
    t = [0]
    for i in range(N):
        v.append(v[i] + (P/(m*v[i]))*dt)
        t.append(t[i] + dt)
    cap = "Bicycle Velocity vs Time (No drag)"
#   returning time array, velocity array, and a string for the plot title
    return t, v, cap


#   Calculates the velocity of a Bicycle vs Time with drag
def bicycle_calc_drag(P, m, dt, N, vo, C, rho, A):
    v = [vo]
    t = [0]
    for i in range(N):
        D = (C*rho*A*v[i]*v[i]/(2*m))*dt
        v.append(v[i] + (P/(m*v[i]))*dt - D)
        t.append(t[i] + dt)
    cap = "Bicycle Velocity vs Time (with drag)"
#   returning time array, velocity array, and a string for the plot title
    return t, v, cap


#   Plots whatever velocity and time arrays passed to it
def bicycle_plot(t, v, cap):
    fig = plt.figure()
    fig.suptitle(cap)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.plot(t, v)
    plt.show()


#   tp, vp, title = bicycle_calc_no_drag(P=400, m=70, dt=0.1, N=2000, vo=4)
tp, vp, title = bicycle_calc_drag(P=400, m=70, dt=0.1, N=2000, vo=4, C=0.5, rho=1.229, A=0.33)
bicycle_plot(tp, vp, title)