geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    res = []
    for string in birds:
        if string not in geese:
            res.append(string)
    return res
