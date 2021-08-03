geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    b = sorted(set(birds), key=birds.index)
    return [s for s in b if s not in geese]
