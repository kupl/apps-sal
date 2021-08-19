geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    for j in geese:
        for i in birds:
            if i == j:
                birds.remove(i)
    return birds
