geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    result = list(filter(lambda x: x not in geese, birds))
    return result
