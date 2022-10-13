import numpy as np
import matplotlib.pyplot as plt

com_year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp_deviation = [0.29, 0.14, 0.19, 0.26, 0.28, 0.22, 0.43, 0.59, 0.33, 0.29]

#ham bac tuyen tinh
def grada(alpha, beta):
    c = 0
    for i in range(10):
        y = com_year[i]
        t = temp_deviation[i]
        c += (2*alpha*y*y + 2*y*(t-beta))
    return c/20

def gradb(alpha, beta):
    c = 0
    for i in range(10):
        y = com_year[i]
        t = temp_deviation[i]
        c += (-2*t + 2*beta + 2*alpha*y)
    return c/20

def GD1(alpha, beta):
    a = [alpha]
    b = [beta]
    eta = 1e-6
    for i in range(10000):
        alpha = alpha - eta*grada(a[-1], b[-1])
        beta = beta - eta*gradb(a[-1], b[-1])
        a.append(alpha)
        b.append(alpha)
        if abs(grada(alpha, beta)) < 1e-3 and abs(gradb(alpha, beta)) < 1e-3:
            break
        
    return (a, b)
plt.scatter(com_year, temp_deviation)
(a, b) = GD1(1/10, 0.3)
print(a[-1], b[-1])
x0 = np.random.randint(low=0, high=15, size=1000)
y0 = a[-1]*x0 + b[-1]
print(x0, y0)
plt.grid()
plt.plot(x0, y0)
plt.show()