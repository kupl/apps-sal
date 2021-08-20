def reverser(sentence):
    emt = ' '
    split_it = sentence.split(' ')
    for word in split_it:
        emt += word[::-1] + ' '
    return emt[1:-1]
