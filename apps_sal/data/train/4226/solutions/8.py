def remove_smallest(numbers):
    return [numbers[i] for i in range(len(numbers)) if i != numbers.index(min(numbers))]
