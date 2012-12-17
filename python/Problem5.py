import operator
from prime import prime_factorization, factorization_union

__author__ = 'Winton'

#We want the smallest number that is divisible by all the numbers from 1 to 20. Therefore, the prime
#factorization of each number from 1 to 20 must be a subset of the prime factorization of our number.

#Because we are looking for the minimal number, we take the number which satisfies the above
#condition and has no other factors.

#map(prime_factorization, xrange(1,21)) ->
# list of prime factorization maps of the numbers from 1 to 20

#reduce(dictionary_union, map(prime_factorization, xrange(1, 21)), {}) ->
# takes that list and pairwise finds the maximum multiplicity for each prime factor. this is the
# prime factorization of our answer

#takes the map of maximal multiplicities and raises each factor to the associated power

#multiplies the result together to get our answer


print reduce(operator.mul, [x ** v for x,v in reduce(factorization_union, map(prime_factorization, xrange(1,21)), {}).iteritems()], 1)