geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    ls = []
    for i in birds:
        if i in geese:
            continue
        ls.append(i)
    return ls
