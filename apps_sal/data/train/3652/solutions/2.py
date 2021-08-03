def button_sequences(seqR, seqB):
    A, B, res = 1, 1, ""
    for x, y in zip(map(int, seqR), map(int, seqB)):
        if A and B and x:
            y = 0
        if A and x and not y:
            res += 'R'
        if B and not x and y:
            res += 'B'
        if not (x and y):
            A, B = not x, not y
    return res
