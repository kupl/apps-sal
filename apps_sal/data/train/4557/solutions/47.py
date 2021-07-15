def row_weights(array):
    t1w = 0
    t2w = 0
    for pos in range(0,len(array)):
        if pos % 2 == 0:
            t1w += array[pos]
        else:
            t2w += array[pos]
    return (t1w, t2w) 
