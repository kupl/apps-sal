geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    return list([w for w in birds if w not in geese])
