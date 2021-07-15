def difference_of_squares(n):
    s1, s2 = 0, 0
    for i in range(1, n + 1):
        s1 += i
        s2 += i ** 2
    return s1 ** 2 - s2
