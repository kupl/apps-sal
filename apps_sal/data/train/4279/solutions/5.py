def group_in_10s(*args):
    return [None if len(y) == 0 else y for y in [sorted([x for x in list(args) if int(x / 10) == i]) for i in range(0, int(max(list(args)) / 10) + 1)]] if args else []
