geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    oplst = []
    for bird in birds:
        if bird not in geese:
            oplst.append(bird)
    return oplst
