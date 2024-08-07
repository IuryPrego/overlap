import numpy as np
import matplotlib.pyplot as plt

def ft(f, k, x, dx):
    y = f(x)
    for i in range(len(y)):
        y[i] *= np.exp(-1j*k*x[i])*dx
    return y

def f(x):
    y = []
    for xj in x:
        y.append(np.exp(-xj**2)) 
    return y

x = np.linspace(-10, 10, 1000)
k = np.linspace(-10,10,1000)

plt.plot(ft(f, k, x, 200/1000))
plt.show()
