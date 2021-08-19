geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    n = []
    for bird in birds:
        if bird not in geese:
            n.append(bird)
    return n
    # go through birds list if matches any in list drop string
    # loop through all birds match place in lists
