geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    out = []
    for el1 in birds:
        if el1 not in geese:
            out.append(el1)
    return out
