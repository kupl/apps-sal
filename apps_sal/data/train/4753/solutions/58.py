geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    new_birds = []
    for animal in birds:
        if animal not in geese:
            new_birds.append(animal)
    return new_birds
