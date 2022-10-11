import numpy as np
import matplotlib.pyplot as plt
import math

coef = [[2, 3, 5], [1, 1, 2], [3, 1, 6]]
x1 = np.linspace(-5,5,100); y1 = (5-2*x1)/3
x2 = np.linspace(-5,5,100); y2 = 2-x2
x3 = np.linspace(-5,5,100); y3 = 6-3*x3
plt.plot(x1, y1, '-r', label='y1=(5-2*x1)/3')
plt.plot(x2, y2, '-r', label='y2 = 2-x2')
plt.plot(x3, y3, '-r', label='y3 = 6-3*x3')


X = [1, 2, 13/7]
Y = [1, 0, 3/7]
plt.scatter(X,Y)
plt.grid()

def calcE(point, coef):
    e = abs(-coef[0]*point[0] - coef[1]*point[1] + coef[2])
    return e**2
    
def kc(x, y):
    p = np.array([x, y])
    c = 0
    for i in range(3):
        c += calcE([ X[i], Y[i] ], coef[i])
    return c

def gradx(x, y):
    cx = 0
    for i in range(3):
        temp = coef[i]
        a = temp[0]; b = temp[1]; c = temp[2]
        cx += (-2*a*c+2*a*a*x+2*a*b*y)
    return cx

def grady(x, y):
    cy= 0
    for i in range(3):
        temp = coef[i]
        a = temp[0]; b = temp[1]; c = temp[2]
        cy += (-2*b*c+2*b*b*y+2*a*b*x)
    return cy

def GD(x0, y0):
    eta = 1e-2
    x = [x0]
    y = [y0]
    for it in range(100000):
        x_new = x[-1] - eta*gradx(x[-1], y[-1])
        y_new = y[-1] - eta*grady(x[-1], y[-1])
        if abs(gradx(x_new, y_new)) < 1e-3 and abs(grady(x_new, y_new)) > 1e-3:
            break
        x.append(x_new)
        y.append(y_new)
    return (x, y)
(x, y) = GD(1.926, 0.185)
plt.scatter(x, y)
plt.show()
