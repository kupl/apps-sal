last_man_standing = l = lambda n: n == 1 or 2 * (n < 4) or 4 * l(n // 4) - 2 * (n % 4 < 2)
