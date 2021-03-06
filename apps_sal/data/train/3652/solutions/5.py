def button_sequences(*seqRB):
    (wasR, wasB, seq) = (0, 0, [])
    for (r, b) in zip(*map(lambda s: map(int, s), seqRB)):
        what = 'BR'[r]
        realeaseOneofTwo = wasR + wasB == 2 and r + b == 1 and (what != seq[-1])
        freshPress = not wasR + wasB and r + b
        switchButtons = b + r == 1 and (wasR, wasB) == (b, r)
        if realeaseOneofTwo or freshPress or switchButtons:
            seq.append(what)
        (wasR, wasB) = (r, b)
    return ''.join(seq)
