def row_weights(array):
    output = [0, 0]
    if len(array) == 1:
        output[0] += array[0]
        return tuple(output)
    else:
        for i in range(0,len(array)):
            if i % 2 == 0:
                output[0]+=array[i]
            else: 
                output[1]+=array[i]
    return tuple(output)
