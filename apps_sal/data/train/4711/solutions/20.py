def zeros(n):
    """ count all factors of 5: 5 10 15 .. 25(count twice as 25 = 5*5) ..... 125 (count three) """
    p = 0
    sum = 0
    while n > 5**p:
        p += 1
        sum += n // (5**p)
    return sum
