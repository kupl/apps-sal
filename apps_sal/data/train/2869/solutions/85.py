def distinct(seq):
    arr = []
    used = set()

    for n in seq:
        if n not in used:
            arr.append(n)
            used.add(n)

    return arr
