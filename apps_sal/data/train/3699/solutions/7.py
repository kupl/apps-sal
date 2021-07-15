def ranks(a):
    ranks = {}
    for rank, x in enumerate(sorted(a, reverse=True), 1):
        if x not in ranks:
            ranks[x] = rank
    return [ranks[x] for x in a]
