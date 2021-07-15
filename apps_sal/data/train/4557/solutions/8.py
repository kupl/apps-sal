def row_weights(array):
    t1 = 0
    t2 = 0
    for i, n in enumerate(array):
        if i%2==0:
            t1+=n
        else:
            t2+=n
    return t1, t2
