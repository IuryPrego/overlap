import numpy as np
import matplotlib.pyplot as plt


def interference(x, y, w, q, f, x0=0, y0=0):
    return np.exp((-(x-x0)**2-(y-y0)**2)/w**2)*np.sin(q*x + f)**2

x = np.linspace(-10,10,1000)
y = np.linspace(-10,10,1000)

X_grid, Y_grid = np.meshgrid(x,y)

i = interference(X_grid, Y_grid, 2, 5, 0)

plt.contourf(i)
plt.show()
