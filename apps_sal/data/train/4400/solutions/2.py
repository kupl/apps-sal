def minimum_steps(numbers, value):
    return sum(sum(sorted(numbers)[:i + 1]) < value for i in range(len(numbers)))
