def sort_ranks(ranks):
    return sorted(ranks, key=lambda x: map(int, x.split('.')))
