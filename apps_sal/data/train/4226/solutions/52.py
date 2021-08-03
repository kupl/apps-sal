def remove_smallest(numbers):
    smallest_number = None if len(numbers) == 0 else sorted(numbers)[0]
    new_list = numbers.copy()
    for x in new_list:
        if x == smallest_number:
            new_list.remove(x)
            break
    return new_list
