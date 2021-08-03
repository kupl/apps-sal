def remove_smallest(numbers):
   # raise NotImplementedError("TODO: remove_smallest")
    lst = []
    if numbers == []:
        return []
    for i in numbers:
        lst.append(i)
    lstmin = min(lst)
    lst.remove(lstmin)
    return lst
