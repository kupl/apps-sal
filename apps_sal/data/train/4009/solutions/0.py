def digits_average(input):
    digits = [int(c) for c in str(input)]
    while len(digits) > 1:
        digits = [(a + b + 1) // 2 for a, b in zip(digits, digits[1:])]
    return digits[0]
