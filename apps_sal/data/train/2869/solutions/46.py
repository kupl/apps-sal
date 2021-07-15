def distinct(seq):
    found = set()
    result = []
    for i in seq:
        if i in found:
            continue
        result.append(i)
        found.add(i)
    return result
