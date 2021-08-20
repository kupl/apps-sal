geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    l = []
    for i in birds:
        if i not in geese:
            l.append(i)
    return l
