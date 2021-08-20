geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    for y in geese:
        if y in birds:
            birds.remove(y)
    return birds
