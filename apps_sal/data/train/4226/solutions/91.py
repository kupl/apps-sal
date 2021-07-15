def remove_smallest(numbers):
    result = numbers.copy()
    if result:
        item = result.pop(result.index(min(result)))
        return result
    else:
        return []
