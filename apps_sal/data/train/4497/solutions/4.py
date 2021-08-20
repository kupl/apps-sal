def positive_to_negative(binary):
    flip = [int(not e) for e in binary]
    for i in range(len(flip) - 1, -1, -1):
        if flip[i] == 0:
            flip[i] = 1
            break
        flip[i] = 0
    return flip
