geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    # your code here
    new = []
    for bird in birds:
        if bird not in geese:
            new.append(bird)
    return new
