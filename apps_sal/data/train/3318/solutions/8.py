def number_of_carries(a, b):
    c = [0]
    while a or b:
        (c, a, b) = (c + [(c[-1] + a % 10 + b % 10) // 10], a // 10, b // 10)
    return sum(c)
