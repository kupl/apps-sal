def to_freud(sentence):
    if len(sentence):
        a = sentence.count(' ') + 1
        return ('sex ' * a).strip()
    else:
        return ''
