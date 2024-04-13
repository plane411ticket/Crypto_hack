import numpy as np

# Khởi tạo các vectơ cơ sở
v = np.array([[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]])

# Khởi tạo danh sách để lưu trữ các vectơ cơ sở trực giao
u = np.zeros_like(v, dtype=float)

# Tính toán vectơ cơ sở trực giao đầu tiên
u[0] = v[0]

# Sử dụng thuật toán Gram-Schmidt để tính toán các vectơ cơ sở trực giao còn lại
for i in range(1, len(v)):
    u[i] = v[i] - sum((np.dot(v[i], u[j]) / np.dot(u[j], u[j])) * u[j] for j in range(i))

# Tính giá trị thứ hai của u4 với 5 chữ số 
flag = round(u[3][1], 5)

print(flag)
