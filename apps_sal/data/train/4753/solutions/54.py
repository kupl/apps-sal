geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    geeseLess = []
    for i in range(len(birds)):
        if birds[i] not in geese:
            geeseLess.append(birds[i])
    return geeseLess
