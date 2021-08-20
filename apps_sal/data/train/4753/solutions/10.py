geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    for i in range(len(geese)):
        if geese[i] in birds:
            ind = birds.index(geese[i])
            birds.pop(ind)
    return birds
