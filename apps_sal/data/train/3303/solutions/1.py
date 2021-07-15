def div_con(x):
    return sum([a for a in x if isinstance(a, int)]) - sum([int(a) for a in x if not isinstance(a, int)])
