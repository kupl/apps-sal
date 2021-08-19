geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    for g in geese:
        for s in birds:
            if s == g:
                birds.remove(g)
    return birds
