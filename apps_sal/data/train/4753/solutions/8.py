geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']


def goose_filter(birds):
    new_list = []
    for word in geese:
        for words in birds:
            if word == words:
                birds.remove(word)
    return birds
