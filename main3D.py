import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy as sc
import sympy as sp

def latex_to_np(fct): 
    x,y = sp.symbols('x y')
    expr = sp.sympify(fct)
    func = sp.lambdify((x, y), expr, 'numpy')
    return func

#def z(x,y):
    #return np.sin(5*x) * np.cos(5*y) / 5

def gradient(x,y,h=1e-6): 
    dz_dx = (z(x+h,y) - z(x-h,y)) / (2*h)
    dz_dy = (z(x,y+h) - z(x,y-h)) / (2*h)
    return dz_dx, dz_dy
    
fct =  input("Formule (format LaTeX): ")
z = latex_to_np(fct)

a0 = float(input("Coordonée x de départ : "))
b0 = float(input("Coordonée y de départ : "))

I1 = float(input("début interval : "))
I2 = float(input("fin interval : "))


c0 = z(a0,b0)
current_pos = (a0,b0,c0)
alpha = 0.01

x = y = np.linspace(I1,I2, 1000)

X, Y = np.meshgrid(x,y)
Z = z(X,Y)

ax = plt.subplot(projection = '3d', computed_zorder=False)

for _ in range(1000):
    X_prime, Y_prime = gradient(current_pos[0], current_pos[1])
    X_new, Y_new = current_pos[0] - alpha*X_prime, current_pos[1] - alpha*Y_prime
    current_pos = (X_new, Y_new, z(X_new, Y_new))

    ax.plot_surface(X,Y,Z, cmap = "plasma", zorder=0)
    ax.scatter(current_pos[0], current_pos[1], current_pos[2], color = "red", zorder=1)
    plt.pause(0.001)
    ax.clear()