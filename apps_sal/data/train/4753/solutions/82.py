geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    s = list()
    for b in birds:
        if b in geese:
            continue
        else:
            s.append(b)
    return s
