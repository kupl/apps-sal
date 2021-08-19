def button_sequences(seqR, seqB):
    (state, s) = ('', '')
    for (r, b) in zip([c == '1' for c in seqR], [c == '1' for c in seqB]):
        if state == 'R' and (not r) or (state == 'B' and (not b)):
            state = ''
        if not state and r:
            (s, state) = (s + 'R', 'R')
        elif not state and b:
            (s, state) = (s + 'B', 'B')
    return s
