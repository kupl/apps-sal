def get_number_of_squares(n):
    sum = 0
    c = 0
    for i in range(1, n + 1):
        sum += i * i
        c += 1
        if sum >= n:
            return c - 1
    return 0
