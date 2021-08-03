def group_in_10s(*args):
    if not args:
        return []
    args = sorted(args)
    lsd = [None] * (max(args) // 10 + 1)
    for i in args:
        if not lsd[i // 10]:
            lsd[i // 10] = [i]
        else:
            lsd[i // 10].append(i)
    return lsd
