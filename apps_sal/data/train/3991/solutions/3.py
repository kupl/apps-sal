def highest_rank(arr):
    best = 0
    occs = 0
    for item in arr:
        times = arr.count(item)
        if times > occs:
            best = item
            occs = times
        elif times == occs:
            if best < item:
                best = item
    return best
