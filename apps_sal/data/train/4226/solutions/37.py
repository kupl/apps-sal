def remove_smallest(numbers):
    if not numbers: return []
    new_lst = numbers.copy()
    new_lst.pop(numbers.index(min(numbers)))
    return new_lst
