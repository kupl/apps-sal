def choose_best_sum(t, k, ls):
    def choice(k, ls):
        import itertools
        return [list(i) for i in itertools.combinations(ls, k)]

    options = choice(k, ls)
    dist_options = []
    for option in options:
        dist_options.append(sum(option))
    dist_options.sort()
    distance = None
    for i in range(len(dist_options)):
        if dist_options[i] > t:
            break
        distance = dist_options[i]
    return distance
