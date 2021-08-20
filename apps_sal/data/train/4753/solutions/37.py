geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    arr = []
    for i in birds:
        if i in geese:
            continue
        else:
            arr.append(i)
    return arr
