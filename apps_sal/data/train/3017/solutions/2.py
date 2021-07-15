def rocks(n):
    cost = 0
    digits = 0
    while n >= 10 ** (digits + 1):
        digits += 1
        cost += (10 ** digits - 10 ** (digits - 1)) * digits
    cost += (n - (10 ** digits) + 1) * (digits + 1)
    return cost
