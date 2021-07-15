geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    notgeese = []
    for el in birds:
        if el not in geese:
            notgeese.append(el)
    return notgeese
