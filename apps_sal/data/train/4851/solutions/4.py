def sort_ranks(ranks):
    return sorted(ranks, key=lambda r: [int(n) for n in r.split(".")])
