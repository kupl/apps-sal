def sort_reindeer(reindeer_names):
    with_last_names = []
    for i in reindeer_names:
        with_last_names.append((i, i.split(' ')[1]))
    return [i[0] for i in sorted(with_last_names, key=lambda x: x[1])]
