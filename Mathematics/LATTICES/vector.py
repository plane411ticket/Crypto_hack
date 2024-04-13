import numpy as np

v = np.array([2, 6, 3])
w = np.array([1, 0, 0])
u = np.array([7, 7, 2])

result = 3 * (2 * v - w) @ (2 * u)

print(result)
