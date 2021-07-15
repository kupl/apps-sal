def smash(words):
    stroke = ''
    for i in words:
        stroke = stroke + i + ' '
    stroke = stroke.rstrip()
    return stroke

