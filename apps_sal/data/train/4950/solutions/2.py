def find_initial_numbers(divisor, iterations):
    a, b = divisor, 0
    for i_iter in range(iterations):
        a, b = a * (divisor + 1) + b, a
    return [a, b]
