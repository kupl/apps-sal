def remove_smallest(numbers):
    result = []
    added = False
    if not numbers:
        return numbers
    for item in numbers:
        if item == min(numbers) and (not added):
            added = True
            continue
        else:
            result.append(item)
    return result
