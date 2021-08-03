def yes_no(ar, i=0):
    red = []
    while ar:
        i = [i, i % max(1, len(ar))][all((ar, i >= len(ar)))]
        red.append(ar.pop(i))
        i += 1
    return red
