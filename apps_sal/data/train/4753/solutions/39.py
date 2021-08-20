geese = set(['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher'])


def goose_filter(birds):
    return [*filter(lambda s: s not in geese, birds)]
