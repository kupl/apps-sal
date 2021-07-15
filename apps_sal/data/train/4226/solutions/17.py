def remove_smallest(numbers):
    res = []
    if len(numbers) == 0:
        return []
    for i in numbers:
        if i == min(numbers):
            res.append(numbers.index(i))
    return numbers[0:min(res)]+numbers[min(res)+1:]

