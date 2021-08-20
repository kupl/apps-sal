def find_missing_number(sequence):
    items = sequence.split(' ')
    try:
        items = sorted((int(x) for x in items)) if sequence else []
    except ValueError:
        return 1
    for (i, x) in enumerate(items, 1):
        if i != x:
            return i
    return 0
