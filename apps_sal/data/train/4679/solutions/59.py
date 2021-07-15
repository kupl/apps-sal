def to_freud(sentence):
    sentence = sentence.split()
    return ('sex ' * len(sentence))[:-1]
