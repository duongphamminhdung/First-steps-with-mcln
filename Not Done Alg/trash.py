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

def calcdist(point, coef):
    d = abs(coef[0]*point[0] + coef[1]*point[1] + coef[2])/math.sqrt(coef[0]**2 + coef[1]**2)
    return d
    
def kc(x, y):
    p = np.array([x, y])
    c = 0
    for i in range(3):
        c += calcdist([ X[i], Y[i] ], coef[i])
    return c

plt.scatter(1.5, 1.5)
plt.show()

