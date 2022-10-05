import numpy as np
import matplotlib.pyplot as plt
# Function for polynomial display
# We do not need pay much attention on this part
def plot_polynomial(xmin, xmax, coef, color='C1'):
    #xs is an array of evenly spaced numbers between xmin and xmax
    xs = np.linspace(xmin, xmax, num=500)
    
    #ys is an array, each element is computed as a polynomial function of
    #the corresponding element of xs
    ys = np.zeros_like(xs)
    for p, c in enumerate(coef.flatten()):
        ys += c*np.power(xs, p)
    plt.plot(xs, ys, color=color)
X0 = np.array([[2], [7], [9], [3], [10], [6], [1], [8]])
ones = np.ones_like(X0)
X = np.concatenate((X0, ones), axis=1)
Y = np.array([[13], [35], [41], [19], [45], [28], [10], [55]])

plt.scatter(X0,Y)

# #normal equation
# theta = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(Y))
# plt.scatter(X0, Y)
# plot_polynomial(0, 10, theta)
# plt.show()

# #Gradient Descent
# m = X.shape[0]
# theta_gd = np.random.normal(size=2).reshape([2,1])
# learning_rate = 0.02
# def grad_cal(X, Y, theta_gd, m):
#     """
#     X: X's value
#     Y: Y's value
#     theta_gd: theta's value
#     m: number of samples
#     """    
#     g = 1/m * X.T.dot(X.dot(theta_gd) - Y)
#     return g.reshape(theta_gd.shape)
# def loss(X, Y, theta_gd, m):
#     """
#     X: X's value
#     Y: Y's value
#     theta_gd: theta's value
#     m: number of samples
#     """
#     return 1/(2*m) * np.sum((X.dot(theta_gd) - Y)**2)
# for i in range(10000):
#     grad_value = grad_cal(X, Y, theta_gd, m)
#     theta_gd = theta_gd - learning_rate*grad_value
#     if (i+1)%1000 == 0:
#         print(loss(X, Y, theta_gd, m))
# print(theta_gd)
# plt.scatter(X0, Y)
# plot_polynomial(0, 10, theta_gd)
# plt.show()