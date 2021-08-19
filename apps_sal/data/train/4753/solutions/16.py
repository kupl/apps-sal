geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    return list(filter(lambda v: not geese.__contains__(v), birds))
