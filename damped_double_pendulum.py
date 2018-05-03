import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


""" User can choose these variables below to alter graph and see results """

gamma = 0.2 #
omega = 2*np.pi # natural frequency
omega0 = 1.5 * omega #
beta = omega0/4
interval = 6 # plot from 0 to interval(seconds) 
U0 = [0, 0] #initial conditions 



"""System of ODE needing to be solved using scipy"""

def dU_dx(U, x, gamma, omega, omega0, beta):

    a = 2*beta
    b = omega0**2
    c = gamma*(omega0**2)
    d = omega 

    return [U[1], -((a*U[1]) + (b*(np.sin(U[0])) - (c*(np.cos(d*x)))))]


""" Intergrating function between interval based on inital conditions """

xs = np.linspace(0, interval, 500) #timesteps 
Us = odeint(dU_dx, U0, xs, args = (gamma,omega, omega0, beta))
ys = Us[:,0]



"""Plotting graph Phi vs Time with gamma value in the legend"""

plt.plot(xs,ys,'green', label = r"$\gamma$ = %.2f" %gamma)
plt.xlabel("Time(s)")
plt.ylabel(r"$\phi$")
plt.title("Driven Damped Pendulum")
plt.grid()
plt.legend(loc='upper right')

plt.show()