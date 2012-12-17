__author__ = 'Winton'
#Difference between sum of squares and square of sums of the firs 100 natural numbers

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6
def sum_of_natural_numbers(n):
    return (n * (n + 1)) / 2

def helper(n):
    return sum_of_natural_numbers(n)**2 - sum_of_squares(n)

print helper(100)