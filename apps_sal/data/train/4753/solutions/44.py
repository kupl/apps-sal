geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    filtered_birds = []
    for i in range(len(birds)):
        if birds[i] in geese:
            None
        else:
            filtered_birds.append(birds[i])
    return filtered_birds
