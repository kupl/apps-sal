def sort_ranks(ranks):
    return sorted(ranks, key=lambda x: [int(y) for y in x.split('.')])
