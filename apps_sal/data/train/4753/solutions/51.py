geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    lonely_birds = []
    for i in birds:
        if i not in geese:
            lonely_birds.append(i)
    return lonely_birds
