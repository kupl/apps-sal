def remove_smallest(numbers):
    if len(numbers) != 0:
        return numbers[:numbers.index(min(numbers))] + numbers[numbers.index(min(numbers))+1:]
    return numbers

