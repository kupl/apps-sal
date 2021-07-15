def sort_ranks(ranks):
    return sorted(ranks, key=lambda s: list(map(int, s.split('.'))))
