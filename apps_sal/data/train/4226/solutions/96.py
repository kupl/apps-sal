def remove_smallest(numbers):
    return [num for i, num in enumerate(numbers) if i != numbers.index(min(numbers))]

