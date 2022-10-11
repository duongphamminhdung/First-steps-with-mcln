import sys
sys.setrecursionlimit(100000)
import numpy as np
N = 5
# matrix = np.array([[ 1., -1., -1., 14., -1.],
#  [-1., 13.,  2., -1., -1.],
#  [-1., -1.,  9. , 6.,  3.],
#  [12.,  7. , 4., -1., 10.],
#  [-1., -1., 11.,  8.,  5.]])
matrix = np.ones((N, N))*(-1)
matrix[0][0] = 1
xMove = [1, 2, 1, 2, -1, -2, -1, -2]
yMove = [2, 1, -2, -1, 2, 1, -2, -1]

def check(x, y):
    return (x >= 0 and y >= 0 and x < N and y < N)
def run(x, y, count, matrix):
    if count == N*N:
        return 1
    for i in range(8):
        xNext = x + xMove[i]
        yNext = y + yMove[i]
        if check(xNext, yNext) and ((matrix[xNext, yNext] == -1)):
            matrix[xNext][yNext] = count+1
            if run(xNext, yNext, count+1, matrix) == 1:
                return 1
            else:
                matrix[xNext][yNext] = -1
    
        # print(matrix)
    return 0
    
run(0 ,0, 1, matrix)
print(matrix)
run(0 ,0, 1, matrix)
print(matrix)