def goose_filter(birds):
    geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']
    newList = []
    for word in birds:
        if word not in geese:
            newList += [word]
    return newList
