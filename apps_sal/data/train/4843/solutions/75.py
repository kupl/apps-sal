def choose_best_sum(t, k, ls):
    import itertools

    best = 0

    candidates = list(itertools.combinations(ls, k))

    for candidate in candidates:
        if sum(candidate) <= t and sum(candidate) > best:
            best = sum(candidate)

        else:
            continue

    if best == 0:
        return None

    else:
        return best

