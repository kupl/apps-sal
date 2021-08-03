def motif_locator(sequence, motif):
    start = 0
    arr = []
    while True:
        index = sequence.find(motif, start)
        if index == -1:
            break
        start = index + 1
        arr.append(index + 1)
    return arr
