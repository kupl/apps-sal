

def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    new = []
    for i in birds:
        if i in geese:
            continue
        else:
            new.append(i)
    return new
