geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    delete_array = []
    for i in range(len(birds)):
        if birds[i] in geese:
            delete_array.append(birds[i])
    for i in delete_array:
        if i in birds:
            birds.remove(i)
    return birds
