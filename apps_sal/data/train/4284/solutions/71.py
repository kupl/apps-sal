def array_leaders(numbers):
    return [n for (i, n) in enumerate(numbers) if n > sum(numbers[i + 1:])]
