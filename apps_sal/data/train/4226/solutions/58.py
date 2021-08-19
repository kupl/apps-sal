def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    x = min(numbers)
    result = []
    first = True
    for num in numbers:
        if num == x and first:
            first = False
        else:
            result.append(num)
    return result
