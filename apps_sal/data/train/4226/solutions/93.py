def remove_smallest(numbers):

    numlist = numbers.copy()

    if len(numlist) <= 1:
        return []
    else:
        numlist.remove(min(numlist))

    return numlist
