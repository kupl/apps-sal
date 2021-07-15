def row_weights(array):
    a = 0
    b = 0
    
    for i, x in enumerate (array):
        if i%2 == 0:
            a = a + x
        else:
            b = b + x
    return a,b
