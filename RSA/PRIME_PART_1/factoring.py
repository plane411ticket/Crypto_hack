import sympy

# The given number
N = 510143758735509025530880200653196460532653147

# Factorize the number
factors = sympy.factorint(N)

# Get the two primes
primes = list(factors.keys())

# Get the smaller prime
smaller_prime = min(primes)

print("The smaller prime is:", smaller_prime)
