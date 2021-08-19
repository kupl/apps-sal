geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    output = []
    for a in birds:
        if a not in geese:
            output.append(a)
    return output
