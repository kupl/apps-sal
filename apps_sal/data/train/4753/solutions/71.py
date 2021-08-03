geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    # your code here
    l = []
    for i in range(0, len(birds)):
        if birds[i] not in geese:
            l.append(birds[i])
    return(l)
