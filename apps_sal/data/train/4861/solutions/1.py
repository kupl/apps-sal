def get_number_of_squares(n):
    (s, i) = (0, 0)
    while s < n:
        i += 1
        s += i ** 2
    return i - 1
