def row_weights(array):
    first=[]
    second=[]
    for i,v in enumerate(array):
        if i%2:
            first.append(v)
        else:
            second.append(v)
    return (sum(second),sum(first))
