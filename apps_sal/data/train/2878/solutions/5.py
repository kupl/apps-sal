def shortest_to_char(alist, target):
    loc = [i for i, x in enumerate(alist) if x == target]
    if not loc:
        return []

    shortest = [min(abs(i - l) for l in loc) for i in range(len(alist))]
    return shortest
