def find_it(seq):
    counts = dict()
    for n in seq:
        if n not in counts:
            counts[n] = 0
        counts[n] += 1
    for (n, n_count) in list(counts.items()):
        if n_count % 2 != 0:
            return n
