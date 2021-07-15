def distinct(seq):
    check = []
    for item in seq:
        if item not in check:
            check.append(item)
    return check
