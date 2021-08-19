def ones_counter(a):
    r = [0]
    for x in a:
        if x == 1:
            r[-1] += 1
        elif r[-1]:
            r.append(0)
    return [x for x in r if x]
