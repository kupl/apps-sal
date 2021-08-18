def largest_power(n):
    print(n)
    if n <= 4:
        if n == 1:
            return (0, -1)
        return (1, -1)

    freq = 0
    x = []
    largest = 0
    j = 0
    while 2**largest < n:
        largest += 1
    largest -= 1
    for i in range(2, largest + 1):
        while j ** i < n:
            j += 1
        j -= 1
        x.append(j**i)
        j = 0

    return (max(x), x.count(max(x)))
