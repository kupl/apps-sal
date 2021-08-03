def find_initial_numbers(divisor, iterations):
    if iterations == 0:
        return divisor, 0
    a, b = divisor, 0
    for _ in range(iterations + 1):
        a, b = a + b, a
    return a, b
