from math import sqrt
from prime import is_prime, remove_factor

__author__ = 'Winton'

def largest_prime(n):
    return largest_prime_helper(n, 1)


def largest_prime_helper(n, start_prime):
    if is_prime(n):
        return n
    for x in xrange(start_prime + 1, int(sqrt(n)) + 1):
        if n % x == 0:
            return largest_prime_helper(remove_factor(n, x)[0], x)
    return start_prime

print largest_prime(600851475143)