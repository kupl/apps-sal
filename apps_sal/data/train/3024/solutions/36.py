def friend(x):
    def friendly(y): return len(y) == 4
    return list(filter(friendly, x))
