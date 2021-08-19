def triple_trouble(one, two, three):
    list_word = []
    for i in range(len(one)):
        list_word.append(one[i])
        list_word.append(two[i])
        list_word.append(three[i])
    return ''.join(list_word)
