def strong_num(n):
    import math
    s = str(n)
    l = map(int, s[:])
    return 'STRONG!!!!' if sum(map(math.factorial, l)) == n else 'Not Strong !!'
