def max_gap(numbers):
    numbers.sort()
    return max((a - b for (a, b) in zip(numbers[1:], numbers[:-1])))
