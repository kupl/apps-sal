def remove_smallest(numbers):
    a = numbers[:]
    if not a:
        return a
    else:
        a.remove(min(a))
        return a
    #raise NotImplementedError("TODO: remove_smallest")
