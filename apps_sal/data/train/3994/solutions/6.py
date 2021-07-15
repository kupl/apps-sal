def nbr_of_laps(x, y):
    a, b = x, y
    remain = a % b
    while remain > 0:
        a, b = b, remain
        remain = a % b
    lcm = x * y / b
    return lcm / x, lcm / y
