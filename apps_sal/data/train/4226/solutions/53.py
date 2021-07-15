def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    na = numbers.copy()
    na.sort()
    sm = na[0]
    rv = numbers.copy()
    rv.remove(sm)
    return rv

