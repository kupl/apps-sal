def sum_of_squares(n):

    def divide_count(p):
        nonlocal n, s1, s2
        while not n % p ** 2:
            n //= p * p
        if not n % p:
            s1 &= False
            s2 &= p & 3 < 3
            n //= p
    s1 = s2 = True
    divide_count(2)
    s3 = n << 1 - s1 & 7 < 7
    divide_count(3)
    (x, wheel) = (5, 2)
    while x * x <= n:
        divide_count(x)
        (x, wheel) = (x + wheel, 6 - wheel)
    if n > 1:
        divide_count(n)
    return 4 - s3 - s2 - s1
