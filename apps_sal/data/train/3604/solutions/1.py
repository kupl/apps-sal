def is_happy(n):
    while n > 4:
        n = sum((d - 48)**2 for d in str(n).encode())
    return n == 1

happy = list(filter(is_happy, range(3 * 10 ** 5)))

from bisect import bisect_right
def performant_numbers(n):
    return happy[:bisect_right(happy, n)]
