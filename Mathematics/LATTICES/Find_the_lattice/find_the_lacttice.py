from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import random
import math
import numpy as np


def Gauss(v1, v2):
	while True:
		if np.inner(v2,v2) < np.inner(v1,v1) : v1, v2 = v2, v1
		m = math.floor(np.inner(v1,v2) / np.inner(v1,v1))
		#print(m,v1,v2)
		if m == 0 : return v1, v2
		v2 = v2 - v1*m


def gen_key():
    q = getPrime(512)
    upper_bound = int(math.sqrt(q // 2))
    lower_bound = int(math.sqrt(q // 4))
    f = random.randint(2, upper_bound)
    while True:
        g = random.randint(lower_bound, upper_bound)
        if math.gcd(f, g) == 1:
            break
    h = (inverse(f, q)*g) % q
    return (q, h), (f, g)
    	
def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m
    
    
fi=open("output.txt",'r')
public=fi.readline().strip()
enc=fi.readline().strip()
enc=int(enc[15:])
print(enc)
public=public[13:-1].split(', ')
q, h = public
q=int(q)
h=int(h)

"""
Tìm cặp (f, g) thỏa f.h = g mod q
=> fh = g+k*q
=> fh-kq = g
=> f(1,h) - k(0,q) = (f,g)
Tìm được hai cơ sở là  (1,h) and (0,q)
"""

v1=np.array([1,h])
v2=np.array([0,q])

u, v = Gauss(v1,v2)

print(u,v)

f=u[0]
g=u[1]

flag=decrypt(q, h, f, g, enc)
print(long_to_bytes(flag))




