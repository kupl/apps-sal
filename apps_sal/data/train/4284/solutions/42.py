def array_leaders(numbers):
    return [val for ind, val in enumerate(numbers) if val > sum(numbers[ind + 1:])]
