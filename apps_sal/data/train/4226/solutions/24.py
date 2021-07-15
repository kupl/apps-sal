def remove_smallest(numbers):
    result = numbers.copy()
    if result:
        result.remove(min(result))
    return result
