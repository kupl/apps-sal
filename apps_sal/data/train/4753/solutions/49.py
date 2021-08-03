import itertools
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    a = [n for n in birds if n not in geese]
    return a
