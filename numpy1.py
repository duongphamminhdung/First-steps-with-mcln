import numpy as np
numbers_1D = np.arange(10)
for item in np.nditer(numbers_1D):
    print(item)
    
numbers_3D = np.random.random((2, 3, 2))
for item in np.nditer(numbers_3D, op_flags = ['readwrite']):    #theem op_flags là readwrite để bật chế độ chỉnh sửa
    item = item **2
    print(item ** 2)

#lặp qua dòng
# order = C => hàng dọc
# order = F => hàng ngang
numbers_2D = np.array([[1, 2], [3, 4], [5, 6]])
for item in np.nditer(numbers_2D, flags = ['external_loop'], order = 'F', op_flags = ['readwrite']): #F
    item **= 2
    print(item)

