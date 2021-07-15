from bisect import bisect_left, bisect_right

EVEN = set('02468')
pedps = [x for x in (x*x for x in range(8, 1000000, 2)) if set(str(x)) <= EVEN]

def even_digit_squares(a, b):
    return pedps[bisect_left(pedps, a):bisect_right(pedps, b)]
