geese = ['Roman Tufted', 'African', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    for goose in geese:
        for bir in birds:
            if goose == bir:
                birds.remove(bir)
    return birds
