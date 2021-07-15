def row_weights(array):
    if len(array) == 1:
        return (array[0],0)
    x = []
    y = []
    for i in range(0,len(array)-1,2):
        x.append(array[i])
        y.append(array[i+1])
    if len(array) % 2 != 0:
        x.append(array[-1])
    return (sum(x),sum(y))
