def to_freud(sentence):
    count = len(sentence.split())
    return ('sex '*count)[:-1]
