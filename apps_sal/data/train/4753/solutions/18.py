geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    list = []
    for x in birds:
        if x not in geese:
            list.append(x)
    return list
