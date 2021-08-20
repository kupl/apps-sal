geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    for elem in geese:
        for bird in birds:
            if elem in birds:
                birds.remove(elem)
    return birds
