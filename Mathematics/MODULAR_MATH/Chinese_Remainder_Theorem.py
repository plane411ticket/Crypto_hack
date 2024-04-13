from Crypto.Util.number import *
"""
x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17
"""
print((2*11*17*inverse(11*17,5) + 3*5*17*inverse(5*17,11) + 5*5*11*inverse(5*11,17)) % 935)