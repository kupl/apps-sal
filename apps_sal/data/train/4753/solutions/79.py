geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    for y in geese:
        for x in birds:
            if x == y:
                birds.remove(x)

    return birds
