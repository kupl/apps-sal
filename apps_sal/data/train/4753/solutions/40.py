geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    without_geese = []
    for i in birds:
        if i not in geese:
            without_geese.append(i)
    return without_geese
