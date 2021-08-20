from itertools import filterfalse
geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    return list(filterfalse(lambda x: x in geese, birds))
