def sum_triangular_numbers(n):
    if n <= 0:
        return 0

    s = 1
    i = 2

    t = 1
    x = 1
    while x < n:
        s += i
        i += 1
        x += 1
        t += s

        #print(s, t)

    return t
