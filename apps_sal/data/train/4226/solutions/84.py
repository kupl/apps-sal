def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    smallest = numbers[0]
    removed = False
    result = []
    for x in numbers:
        if x < smallest:
            smallest = x
    for x in numbers:
        if x == smallest and not removed:
            removed = True
            continue
        result.append(x)
    return result


