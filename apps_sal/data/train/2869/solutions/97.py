def distinct(seq):
    test = set()
    unique = []
    for x in seq:
        if x not in test:
            unique.append(x)
            test.add(x)
    return unique

