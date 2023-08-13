import numpy as np 
import matplotlib.pyplot as plt
import sympy as sp

def z(x,y):
    return np.sin(5*x) * np.cos(5*y) / 5

def gradient(x,y): 
    return np.cos(5*x)*np.cos(5*y), -np.sin(5*x) * np.sin(5*y)


x = y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x,y)
Z = z(X,Y)

a0 = 0.7
b0 = 0.4
c0 = z(a0,b0)
current_pos = (a0,b0,c0)
alpha = 0.01

ax = plt.subplot(projection = '3d', computed_zorder=False)

for _ in range(1000):
    X_prime, Y_prime = gradient(current_pos[0], current_pos[1])
    X_new, Y_new = current_pos[0] - alpha*X_prime, current_pos[1] - alpha*Y_prime
    current_pos = (X_new, Y_new, z(X_new, Y_new))

    ax.plot_surface(X,Y,Z, cmap = "plasma", zorder=0)
    ax.scatter(current_pos[0], current_pos[1], current_pos[2], color = "red", zorder=1)
    plt.pause(0.001)
    ax.clear()