__author__ = 'Winton'
from prime import prime_factorization
#We are asked to find the first four consecutive numbers with four distinct primes.
#def consecutive_with_primes(n,k):
#    start = 2
#    while True:
#        dictionary_union



def distinct_primes(x, n):
    return len(prime_factorization(x).keys()) == n

def consecutive_distinct_prime(n, k):
    i = n+2
    consecutive = [distinct_primes(x, k) for x in xrange(2, n + 2)]
    while True:
        if all(x for x in consecutive):
            return i - n
        consecutive[i % n] = distinct_primes(i, k)
        i += 1

print(consecutive_distinct_prime(4, 4))
