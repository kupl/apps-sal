geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return [words for words in birds if all(char not in words for char in geese)]
