def remove_smallest(numbers):
    if numbers == []:
        return numbers
    new_lst = list(numbers)
    smallest = min(new_lst)
    del new_lst[new_lst.index(smallest)]
    return new_lst
