geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    for i in geese:
        try:
            birds.remove(i)
        except:
            pass
    return birds
