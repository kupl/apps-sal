def find_initial_numbers(divisor, iterations):
    # 5 is a randomly choosen num not a must
    # using different num will give different result but still correct
    a, b = 5 * divisor, divisor
    for i in range(1, iterations):
        a, b = 5 * a + b, a
    return (a, b) if iterations else (divisor, iterations)
