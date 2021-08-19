def remove_smallest(numbers):
    return [n for (i, n) in enumerate(numbers) if i != numbers.index(min(numbers))]
