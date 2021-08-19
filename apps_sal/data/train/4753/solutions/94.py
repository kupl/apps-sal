geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    a = []
    for i in birds:
        if i not in geese:
            a.append(i)
    return a
