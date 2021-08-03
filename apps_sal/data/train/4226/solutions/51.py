def remove_smallest(numbers):
    new_list = numbers.copy()
    if numbers != []:
        new_list.sort()
        min = new_list[0]
        new_list = numbers.copy()
        new_list.remove(min)
    return new_list
