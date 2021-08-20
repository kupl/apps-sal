def find_initial_numbers(divisor, iterations):
    (a, b) = (divisor, 0)
    for _ in range(iterations + (1 if iterations else 0)):
        (a, b) = (a + b, a)
    return (a, b)
