def how_many_measurements(n):
    x = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 3
            first = round(n)
            if n > first:
                n = first + 1
            x += 1
        else:
            n = n / 3
            x += 1
    return x
