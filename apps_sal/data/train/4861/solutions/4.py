def get_number_of_squares(limit):
    total = 1
    for n in range(2, limit + 2):
        if total >= limit:
            return n - 2
        total += n**2
