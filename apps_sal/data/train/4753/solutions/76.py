geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
c = []


def goose_filter(birds):
    for x in geese:
        if x in birds:
            birds.remove(x)
    return birds
# your code here
