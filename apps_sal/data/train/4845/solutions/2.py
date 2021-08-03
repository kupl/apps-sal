def sort_nested_list(array):
    numbers = iter(sorted(n for a1 in array for a2 in a1 for n in a2))
    return [[[next(numbers) for n in a2] for a2 in a1] for a1 in array]
