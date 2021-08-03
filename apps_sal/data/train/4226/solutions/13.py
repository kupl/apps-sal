def remove_smallest(numbers):
    if len(numbers) <= 1:
        return []
    result = []
    min_index_v = numbers.index(min(numbers))
    for number in enumerate(numbers):
        if number[0] != min_index_v:
            result.append(number[1])
    return result
