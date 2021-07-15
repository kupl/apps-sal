geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    l = []
    for n in birds:
        if n not in geese:
            l.append(n)
    return l
