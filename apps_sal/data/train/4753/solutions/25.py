geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    for word in geese:
        while word in birds:
            birds.remove(word)
    return birds
