geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    return list((birds[i] for i in range(len(birds)) if birds[i] not in geese))
