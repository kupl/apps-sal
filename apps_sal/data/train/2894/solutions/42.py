def triple_trouble(one, two, three):
    word = ''
    for i in range(0, len(one)):
        word += one[i] + two[i] + three[i]
    return word
