def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    new=[]
    for x in birds:
        if x not in geese:
            new.append(x)
    return new
