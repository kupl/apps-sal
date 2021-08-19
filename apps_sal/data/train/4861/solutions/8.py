def get_number_of_squares(n):
    (res, i) = (0, 0)
    while res < n:
        res += i ** 2
        i += 1
    return i - 2
