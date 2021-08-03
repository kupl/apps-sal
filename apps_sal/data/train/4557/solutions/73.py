def row_weights(array):
    w1, w2 = [0], [0]
    for key, i in enumerate(array):
        w1.append(i) if key % 2 == 0 else w2.append(i)
    return (sum(w1), sum(w2))
