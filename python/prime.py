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

#Finds the LCM of q series of numbers based on their prime factorizations
def factorization_union(dict1, dict2):
    union = {}
    for k in dict1.keys():
        if k not in dict2:
            union[k] = dict1[k]
        else:
            union[k] = max(dict1[k], dict2[k])
    for k2 in dict2.keys():
        if k2 not in dict1:
            union[k2] = dict2[k2]
    return union

#Implementation of the sieve of Eratosthenes, O(n log (log (n))) algorithm for finding the primes
#less than n.
def sieve(n):
    A = set(xrange(2, n))
    for x in xrange(2, n):
        if x in A:
            for y in xrange(2 * x, n, x):
                if y in A:
                    A.remove(y)
    return A

#TODO Expand this so that it runs the sieve on 10000 numbers stores the primes, and goes through
# the next 10000.
def find_nth_prime(n):
    p = 0
    A = set(xrange(2, 1000000))
    for x in xrange(2, 1000000):
        if x in A:
            p += 1
            if p == n:
                return x
            for y in xrange(2 * x, 1000000, x):
                if y in A:
                    A.remove(y)
    return 0
