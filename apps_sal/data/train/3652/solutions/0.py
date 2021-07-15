def button_sequences(seqR, seqB):
    pattern, state = '', ''
    toBool = lambda seq : [i == '1' for i in seq]
    for red, blue in zip(toBool(seqR), toBool(seqB)):
        if red and state == 'R' or blue and state == 'B':
            continue
        state = 'R' if red else 'B' if blue else ''
        pattern += state
    return pattern
