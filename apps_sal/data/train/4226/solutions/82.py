def remove_smallest(numbers):
    result = list(numbers)
    if len(numbers) >= 1:
        result.remove(min(numbers))
    else:
        return ([])
    return result
