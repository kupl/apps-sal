def square_free_part(n):
    if type(n) != int or n < 1:return None
    for i in xrange(2, int(n ** 0.5) + 1):
        while n % (i ** 2) == 0:
            n /= i
    return n
