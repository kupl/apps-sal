def remove_smallest(numbers):
    if not numbers:
        return numbers
    result = numbers.copy()
    smolest = list(set(numbers))
    smolest.sort()
    result.remove(smolest[0])
    return result
