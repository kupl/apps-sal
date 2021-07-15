def sum_arrays(*args):
    if all(x == [] for x in args) or all(x == [0] for x in args):
        return []
    elif any(x == [] for x in args):
        return max(args)
    else:
        s = sum(int(''.join(map(str, x))) for x in args)
        minus = s < 0
    return [int(x) * -1 if minus and i == 0 else int(x)
                        for i, x in enumerate(list(str(abs(s))))]

