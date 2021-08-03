def get_number_of_squares(n):
    k = 1
    while k * (k + 1) * (2 * k + 1) / 6 < n:
        k += 1
    return k - 1
