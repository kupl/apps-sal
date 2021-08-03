geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds: list) -> list:
    return [x for x in birds if x not in geese]
