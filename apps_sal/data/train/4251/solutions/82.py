def difference_of_squares(n):
    # ...
    total = 0
    sums = 0
    for i in range(1, n + 1):
        sums += i ** 2
        total += i
    return total ** 2 - sums

