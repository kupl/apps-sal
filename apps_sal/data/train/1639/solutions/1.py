def gta(limit, *args):
    args = [str(n).ljust(limit, '.') for n in args]
    (unique, frequency, fact) = (set(), 0, 1)
    for c in zip(*args):
        for d in c:
            if d == '.' or d in unique:
                continue
            limit -= 1
            unique.add(d)
            frequency += fact * len(unique)
            fact *= limit
            if not limit:
                return frequency * sum(map(int, unique))
