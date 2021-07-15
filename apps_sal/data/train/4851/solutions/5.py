def sort_ranks(ranks):
    return sorted(ranks, key = lambda x: tuple(map(int, x.split('.'))))
