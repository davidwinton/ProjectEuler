from math import sqrt

__author__ = 'Winton'

def is_prime(n):
    if n == 1 or not n == 2 and n % 2 == 0:
        return False
    for x in xrange(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True


def factor_multiplicity(n, d):
    return remove_factor(n, d)[1]


def remove_factor(n, d):
    count = 0
    while n % d == 0:
        n = n / d
        count += 1
    return n, count


def largest_prime(n, start_prime):
    if is_prime(n):
        return n
    for x in xrange(start_prime + 1, int(sqrt(n)) + 1):
        if n % x == 0:
            return largest_prime(remove_factor(n, x)[0], x)
    return start_prime


def prime_factorization(n):
    L = {}
    return prime_factorization_helper(n, 1, L)


def prime_factorization_helper(n, start_prime, accumulator ):
    if is_prime(n):
        accumulator[n] = 1
        return accumulator
    for x in xrange(start_prime + 1, int(sqrt(n)) + 1):
        if n % x == 0:
            new_num, count = remove_factor(n, x)
            accumulator[x] = count
            return prime_factorization_helper(new_num, x, accumulator)
    return accumulator
