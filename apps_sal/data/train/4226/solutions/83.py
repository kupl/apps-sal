def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    idx = numbers.index(min(numbers))
    return numbers[:idx] + numbers[idx + 1:]
