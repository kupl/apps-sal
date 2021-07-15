def find_a_b(numbers, c):
    return next(([a, c//a] for i, a in enumerate(numbers, 1) if a and c / a in numbers[i:]), None)
