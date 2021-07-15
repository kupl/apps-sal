geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    for x in geese:
        for x in birds:
            if x in geese:
                birds.remove(x)
    return(birds)

