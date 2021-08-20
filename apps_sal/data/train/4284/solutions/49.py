def array_leaders(numbers):
    return [v for (i, v) in enumerate(numbers) if v > sum(numbers[i:]) - v]
