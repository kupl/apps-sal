last_man_standing=l=lambda n, left=True:n == 1 or 2 * l(n // 2, not left) - (not (n % 2 or left))
