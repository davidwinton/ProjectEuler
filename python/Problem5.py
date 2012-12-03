import operator
from prime import prime_factorization

__author__ = 'Winton'
def dictionary_union(dict1, dict2):
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


print reduce(operator.mul, [x ** v for x,v in reduce(dictionary_union, map(prime_factorization, xrange(1,21)), {}).iteritems()], 1)