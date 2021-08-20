def big_primefac_div(n):
    if n % 1 != 0:
        return 'The number has a decimal part. No Results'
    n = -n if n < 0 else n
    biggest_divisor = 1
    biggest_primefactor = 1
    if n % 2 == 0:
        biggest_primefactor = 2
    elif n % 3 == 0:
        biggest_primefactor = 3
    else:
        i = 5
        while i * i <= n:
            if n % i == 0:
                biggest_primefactor = i
                break
            elif n % (i + 2) == 0:
                biggest_primefactor = i + 2
                break
            i = i + 6
    if biggest_primefactor == 1:
        return []
    biggest_divisor = n / biggest_primefactor
    n = int(n)
    while n % 2 == 0:
        biggest_primefactor = 2
        n >>= 1
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            biggest_primefactor = i
            n = n / i
    if n > 2:
        biggest_primefactor = n
    return [biggest_primefactor, biggest_divisor]
