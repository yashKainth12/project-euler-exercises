#largest prime factor of 600851475143
 #largest prime factor 600851475143
import math

def compute():
    n = 600851475143
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n //= p
        else:
            return n  # Return the largest prime factor directly

def smallest_prime_factor(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return i
    return n  # n itself is prime

compute()

#correct
    












