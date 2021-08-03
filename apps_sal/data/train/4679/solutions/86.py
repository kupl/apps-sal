def to_freud(sentence):
    word = ' sex'
    if sentence.count(' ') == 0:
        return 'sex'
    elif sentence.count(' ') >= 1:
        return 'sex' + word * sentence.count(' ')
