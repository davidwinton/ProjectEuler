__author__ = 'Winton'
#find the product of the only Pythagorean triplet where a + b + c = 1000

def euclid_pythagorean_generator(m,n):
    return m**2-n**2, 2 * m * n, m**2 + n **2

def pythagorean_triple_with_sum(n):
    for i in xrange(1, n):
        for j in xrange(i, n):
            a,b,c = euclid_pythagorean_generator(j,i)
            if a + b + c == n:
                return a * b * c

print pythagorean_triple_with_sum(1000)