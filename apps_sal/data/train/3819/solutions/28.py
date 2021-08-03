def smash(words):
    sentence = ''
    for i in words:
        if words[0] == i:
            sentence += i
        else:
            sentence += f' {i}'
    return sentence
