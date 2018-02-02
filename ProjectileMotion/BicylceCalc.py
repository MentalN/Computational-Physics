#   File: BicycleCalc.py
#   Author: Nawaf Abdullah
#   Creation Date: 2/Feb/2018
#   Description: calculates velocity and time for a bicylce example given power,
#                mass, time step, and total number of steps.
import matplotlib.pyplot as plt


#   Calculates the velocity of a Bicycle vs Time with no drag
def bicycle_calc_no_drag(P, m, dt, N, vo):
    v = [vo]
    t = [0]
    for i in range(N):
        v.append(v[i] + (P/(m*v[i]))*dt)
        t.append(t[i] + dt)
    return t, v


#   Plots whatever velocity and time arrays passed to it
def bicycle_plot(t, v):
    fig = plt.figure()
    fig.suptitle("Bicycle Velocity vs Time")
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.plot(t, v)
    plt.show()


tp, vp = bicycle_calc_no_drag(P=400, m=70, dt=0.1, N=2000, vo=4)
bicycle_plot(tp, vp)