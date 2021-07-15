geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    result = []
    for i in geese:
        for j in birds:
            if i == j:
                birds.remove(i)
    #your code here
    return birds

