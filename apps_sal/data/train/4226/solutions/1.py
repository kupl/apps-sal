def remove_smallest(numbers):
    if len(numbers) < 1:
        return numbers
    idx = numbers.index(min(numbers))
    return numbers[0:idx] + numbers[idx + 1:]
