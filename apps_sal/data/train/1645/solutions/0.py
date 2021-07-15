def one_square(n):
    return round(n ** .5) ** 2 == n

def two_squares(n):
    while n % 2 == 0: n //= 2
    p = 3
    while p * p <= n:
        while n % (p * p) == 0:
            n //= p * p
        while n % p == 0:
            if p % 4 == 3: return False
            n //= p
        p += 2
    return n % 4 == 1

def three_squares(n):
    while n % 4 == 0: n //= 4
    return n % 8 != 7

def sum_of_squares(n):
    if one_square(n): return 1
    if two_squares(n): return 2
    if three_squares(n): return 3
    return 4
