def four_piles(n, y):
    return (lambda x, m: ((x > y) > x % y + m) * [x + y, x - y, x * y, x / y])(*divmod(n * y, y * y + 2 * y + 1))
