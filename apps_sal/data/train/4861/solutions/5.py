def get_number_of_squares(n):
    i, j, k = 1, 1, 1
    while k < n:
        i += 2
        j += i
        k += j
    return i >> 1

