def get_number_of_squares(n):
    s = 0
    i = 0
    while s < n:
        i += 1
        s += i * i
    return i - 1
