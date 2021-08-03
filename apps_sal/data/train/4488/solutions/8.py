def bucketize(*args):
    d = {i: [] for i in range(len(args) + 1)}
    for x in sorted(set(args)):
        d[args.count(x)].append(x)
    return [i if i else None for i in d.values()]
