def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    x = min(numbers)
    for i in range(0, len(numbers)):
        if numbers[i] == x:
            return numbers[:i] + numbers[i + 1:]
