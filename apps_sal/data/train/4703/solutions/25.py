def bar_triang(a, b, c):
    return list(map(lambda p: round(sum(p) / 3, 4), zip(*(a, b, c))))
