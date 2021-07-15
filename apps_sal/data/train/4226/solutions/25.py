def remove_smallest(numbers):
    if numbers == []:
        return numbers
    elif len(numbers) == 1:
        return []

    else:
        copy = numbers[::]
        copy.remove(min(numbers))
        return copy
