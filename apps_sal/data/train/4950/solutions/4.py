def find_initial_numbers(divisor, iterations):
    a, b = 5 * divisor, divisor
    for i in range(1, iterations):
        a, b = 5 * a + b, a
    return (a, b) if iterations else (divisor, iterations)
