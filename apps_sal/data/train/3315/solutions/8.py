def strongest_even(n, m):
    pow = 1
    while pow <= m:
        pow *= 2
    if pow/2 <= m and pow/2 >= n:
        return pow/2
    else:
        pow /= 4
        multiplier = 3
        while True:
            multiple = pow * multiplier
            while multiple <= m:
                if n <= multiple:
                    return multiple
                else:
                    multiplier += 1
                    multiple = pow * multiplier
            pow /= 2
            multiple = 3

