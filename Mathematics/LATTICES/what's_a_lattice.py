import numpy as np

v1 = np.array([6, 2, -3])
v2 = np.array([5, 1, 4])
v3 = np.array([2, 7, 1])

A = np.array([v1, v2, v3])

volume = np.abs(np.linalg.det(A))

print(round(volume))
