def to_freud(sentence):
    x = len(sentence.split(' '))
    return ('sex ' * x).rstrip()
