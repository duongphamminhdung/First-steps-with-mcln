import numpy as np
import matplotlib.pyplot as plt

x0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #com_year
y0 = [0.29, 0.14, 0.19, 0.26, 0.28, 0.22, 0.43, 0.59, 0.33, 0.29] #temperatur deviation
plt.scatter(x0, y0)
#ham bac 2
def grada(a, b, c):
    A = 0
    for i in range(10):
        x = x0[i]; y = y0[i]
        A += 2*a*(x**4) + 2*b*(x**3) - 2*y*x*x + 2*c*x*x
    return A/20

def gradb(a, b, c):
    B = 0
    for i in range(10):
        x = x0[i]; y = y0[i]
        B += 2*a*(x**3) + 2*b*x*x - 2*x*y + 2*c*x
    return B/20    
    
def gradc(a, b, c):
    C = 0
    for i in range(10):
        x = x0[i]; y = y0[i]
        C += -2*y + 2*c + 2*a*x*x + 2*b*x
    return C/20

def GD2(a, b, c):
    a0 = [a]
    b0 = [b]
    c0 = [c]
    eta = 1e-5
    for i in range(100000):
        a = a - eta*grada(a0[-1], b0[-1], c0[-1])
        b = b - eta*gradb(a0[-1], b0[-1], c0[-1])
        c = c - eta*gradc(a0[-1], b0[-1], c0[-1])
        a0.append(a)
        b0.append(b)
        c0.append(c)
        if abs(grada(a, b, c)) < 1e-3 and abs(gradb(a, b, c)) < 1e-3 and abs(gradc(a, b, c)) < 1e-3:
            break
        
    return (a0, b0, c0)

(a0, b0, c0) = GD2(0, 0, 0)
x = 12*np.random.random_sample(size=100)+1
y = a0[-1]*x*x + b0[-1]*x + c0[-1]
print(x, y)
print(a0[-1], b0[-1], c0[-1])
plt.grid()
plt.scatter(x, y)
plt.show()