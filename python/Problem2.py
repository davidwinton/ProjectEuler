from math import sqrt

__author__ = 'Winton'
fibonacci_map = {0:0, 1:1}
def fib(n):
    if n not in fibonacci_map:
        fibonacci_map[n] = fib(n-1) + fib(n-2)
    return fibonacci_map[n]

print sum( [fib(x) for x in xrange(34) if fib(x) % 2 ==0])