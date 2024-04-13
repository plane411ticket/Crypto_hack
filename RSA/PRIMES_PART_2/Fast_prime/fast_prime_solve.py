from math import gcd
from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b//a) * x, x)


key = RSA.importKey(open("key_17a08b7040db46308f8b9a19894f9f95.pem", "rb").read())

n = key.n
e = key.e

c = bytes.fromhex("249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28")

print(" n:", n)

# n is vulnerable to ROCA attack
# neca key.n
# https://gitlab.com/jix/neca
p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
q = 77342270837753916396402614215980760127245056504361515489809293852222206596161

print(" n factored!")
print(" p:", p)
print(" q:", q)

assert p * q == n


phi = (q-1) * (p-1)
_,a,b = egcd(phi, e)

d = b % phi
print(" d:", d)


key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)

print("flag:", cipher.decrypt(c))