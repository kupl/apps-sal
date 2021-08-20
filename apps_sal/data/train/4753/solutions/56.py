geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    n = []
    for i in birds:
        if i not in geese:
            n.append(i)
    return n
