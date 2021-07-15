geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    l=[]
    g=[]
    for x in birds:
        if x in geese:
            l.append(birds.index(x))
    for i in range(len(birds)):
        if i not in l:
            g.append(birds[i])
    return g
