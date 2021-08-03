def bad_apples(apples):
    apples = [list(filter(None, xs)) for xs in apples]
    apples = list(filter(None, apples))
    idxs = [i for i, x in enumerate(apples) if len(x) == 1]
    if len(idxs) % 2 == 1:
        del apples[idxs.pop()]
    for i in reversed(range(0, len(idxs), 2)):
        apples[idxs[i]].append(apples.pop(idxs[i + 1]).pop())
    return apples
