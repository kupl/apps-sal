def stringy(size):
    size - int(size)
    counter = 1
    word = ''
    while len(word) < size:
        if counter % 2 == 0:
            word = word + '0'
        if counter % 2 != 0:
            word = word + '1'
        counter += 1
    return word
