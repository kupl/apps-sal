def between_extremes(numbers):
    numbers.sort()
    b = numbers[-1] - numbers[0]
    return b
