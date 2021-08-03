geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    newlist = []
    for eachvalue in birds:
        if eachvalue in geese:
            continue
        else:
            newlist.append(eachvalue)
    return newlist
