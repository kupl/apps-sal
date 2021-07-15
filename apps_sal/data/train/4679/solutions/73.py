def to_freud(sentence):
    words = sentence.split(' ')
    made_string = str(''.join('sex ' * len(words)))
    return made_string.rstrip()
