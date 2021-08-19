def sum_of_squares(n):
    # three-square theorem
    if n**0.5 == int(n**0.5):
        return 1
    while n % 4 == 0:
        n >>= 2
    if (n - 7) % 8 == 0:
        return 4
    for s in range(1, int(n**0.5) + 1):
        if (n - s * s)**0.5 == int((n - s * s)**0.5):
            return 2
    return 3
