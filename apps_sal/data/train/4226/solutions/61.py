def remove_smallest(numbers):
    #raise NotImplementedError("TODO: remove_smallest")
    if numbers == []: return []
    else:
        a = numbers.copy()
        b = a.remove(min(a))
        return a

