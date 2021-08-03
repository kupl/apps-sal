geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    x = []
    for i in range(len(birds)):
        if birds[i] in geese:
            x = x
        else:
            x.append(birds[i])
    return x
