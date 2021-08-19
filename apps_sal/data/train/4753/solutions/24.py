geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    return [el for (i, el) in enumerate(birds) if el not in geese]
