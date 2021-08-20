def ranks(results):
    ranks = {}
    for (k, v) in enumerate(sorted(results, reverse=True), start=1):
        if not v in ranks:
            ranks[v] = k
    return [ranks[i] for i in results]
