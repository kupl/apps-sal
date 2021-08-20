def array_leaders(numbers):
    return [item for (ind, item) in enumerate(numbers) if item > sum(numbers[ind + 1:])]
