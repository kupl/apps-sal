def unique_in_order(iterable):
    unique = []
    last = ''
    for item in iterable:
        if item != last:
            unique.append(item)
            last = item
    return unique
