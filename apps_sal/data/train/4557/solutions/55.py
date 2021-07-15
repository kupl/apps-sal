def row_weights(array):
    ans = [0 , 0]
    for index in range(0, len(array)):
        if index % 2 == 0:
            ans[0] += array[index]
        else:
            ans[1] += array[index]    
    return tuple(ans)

