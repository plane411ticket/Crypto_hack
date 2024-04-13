import numpy as np
import math

def Gauss(v1, v2):
	while True:
		if np.dot(v2,v2) < np.dot(v1,v1) : v1, v2 = v2, v1
		m = math.floor(np.dot(v1,v2) / np.dot(v1,v1))
		if m == 0 : return v1, v2
		v2 = v2 - v1*m
		
v1=np.array([846835985, 9834798552], dtype=np.int64)
v2=np.array([87502093, 123094980], dtype=np.int64)

u, v = Gauss(v1,v2)
print(np.dot(u, v))
