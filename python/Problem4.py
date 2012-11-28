__author__ = 'Winton'

def is_palindrome(n):
    forward = str(n)
    return forward == ''.join(reversed(forward))

max_pal = 0
for x in xrange(1000, 100, -1):
    for y in xrange(1000, 100, -1):
        if is_palindrome(x * y):
            if max_pal < x * y:
                max_pal = x * y
            break
print max_pal
