def difference_of_squares(n):
    a = 0
    s = 0
    for i in range(n + 1):
        a += i
        s += i * i
    return a * a - s
