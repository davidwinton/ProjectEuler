import operator
from prime import prime_factorization

__author__ = 'Winton'
#What is the first triangle number to have over 500 divisors.

#We use the prime factorization to find the number of divisors.For each factor p, with multiplicity
#m, there are m+1 divisors we can generate (0 to m copies of p in the prime factorization of that
#divisor.

def number_of_divisors(n):
    return reduce(operator.mul, [v + 1 for v in prime_factorization(n).values()], 1)

def first_n_divisor_triangle(n):
    x = 1
    while True:
        triangle = (x * (x+1))/2
        if(number_of_divisors(triangle)) >= 500:
            return triangle
        else:
            x += 1

print first_n_divisor_triangle(500)
