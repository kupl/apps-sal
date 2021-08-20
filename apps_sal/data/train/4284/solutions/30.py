def array_leaders(numbers):
    numbers.append(0)
    return [n for (i, n) in enumerate(numbers[:-1]) if n > sum(numbers[i + 1:])]
