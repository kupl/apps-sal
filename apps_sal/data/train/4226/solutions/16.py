def remove_smallest(numbers):
    tmp = list(numbers)
    if tmp:
        tmp.remove(min(numbers))
    return tmp
