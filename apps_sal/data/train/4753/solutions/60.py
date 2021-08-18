geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    n = []
    for bird in birds:
        if bird not in geese:
            n.append(bird)
    return n
