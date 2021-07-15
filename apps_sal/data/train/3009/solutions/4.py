def pairs(numbers):
    return sum(abs(a - b) == 1 for a, b in zip(numbers[::2], numbers[1::2]))
