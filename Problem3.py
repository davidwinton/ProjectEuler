from math import sqrt

__author__ = 'Winton'
from prime import is_prime

def largest_prime_factor(n):
    return largest_prime(n, 1)


def largest_prime(n, start_prime):
    if is_prime(n):
        return n
    for x in xrange(start_prime + 1, int(sqrt(n)) + 1):
        if n % x == 0:
            return largest_prime(remove_factor(n, x), x)
    return start_prime

def remove_factor(n, d):
    while n % d == 0:
        n = n / d
    return n

print largest_prime_factor(600851475143)