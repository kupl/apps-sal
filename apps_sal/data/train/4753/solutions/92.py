def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    for bir in geese:
        if bir in birds:
            birds.remove(bir)
    return birds
