geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    list = []
    for word in birds:
        if not word in geese:
            list.append(word)
    return list
