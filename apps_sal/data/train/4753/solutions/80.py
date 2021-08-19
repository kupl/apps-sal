geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(words):
    clean = []
    for x in words:
        if x not in geese:
            clean.append(x)
    return clean
