geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    arr = []
    for strn in birds:
        if strn not in geese:
            arr.append(strn)
    return arr
