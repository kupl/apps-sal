def row_weights(array):
    totals = [0,0]
    for int, x in enumerate(array):
        if int % 2 == 0:
            totals[0]+= x
        else:
            totals[1] += x
    return tuple(totals)
