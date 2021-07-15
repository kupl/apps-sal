def remove_smallest(numbers):
    if numbers == []:
        return numbers
    list_copy = numbers.copy()
    list_copy.remove(min(list_copy))
    return list_copy
