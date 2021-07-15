def difference_of_squares(n):
    a = b = 0
    for i in range(1, -~n):
        a += i
        b += i * i
    return abs(a * a - b)
