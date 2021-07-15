def get_number_of_squares(n):
    sm = 0
    i = 0
    while n > sm:
        i += 1
        sm += i ** 2
    return i - 1
