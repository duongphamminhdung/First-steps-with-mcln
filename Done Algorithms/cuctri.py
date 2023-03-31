import numpy as np
import matplotlib.pyplot as plt
import math

def grad(x):
    h = 1e-5
    return (calc(x+h)-calc(x))/2*h

def calc(x):
    return 800*( (16+x**2)**(-3/2)+(16+(6-x)**2)**(-3/2) )

x0 = [0]
y0 = [calc(0)]
ansx = []
def GD(x, y):
    for i in range(600):
        x_new = x0[-1] + 0.01
        x0.append(x_new)
        y0.append(calc(x0[-1]))
        if grad(x0[-1]) > 0 and grad(x0[-1]+0.015) < 0:
            ansx.append(x0[-1])
            
    return (x0, y0, ansx)
(x, y, ans) = GD(x0[-1], y0[-1])
maxi = [calc(i) for i in ans]
plt.plot(x, y)
plt.scatter(ansx, maxi)
plt.show()
