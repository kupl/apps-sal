def array_leaders(numbers):
    return [i for (ind, i) in enumerate(numbers) if i > sum(numbers[ind + 1:])]
