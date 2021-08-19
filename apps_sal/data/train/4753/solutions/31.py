geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    s = []
    for el in birds:
        if not el in geese:
            s.append(el)
    return s
