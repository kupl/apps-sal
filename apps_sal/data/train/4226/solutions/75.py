def remove_smallest(numbers):
    if numbers == []:
        return []
    current_lowest = numbers[0]
    for number in numbers:
        if current_lowest > number:
            current_lowest = number
    removed = []
    condition = 1
    for number in numbers:
        if number == current_lowest and condition == 1:
            condition = 0
        else:
            removed.append(number)
    return removed
    raise NotImplementedError('TODO: remove_smallest')
