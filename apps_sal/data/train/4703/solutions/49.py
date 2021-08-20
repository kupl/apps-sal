def bar_triang(*p):
    return list([round(sum(x) / 3, 4) for x in zip(*p)])
