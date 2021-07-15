def every(array, interval=1, start_index=0):
    res = []
    for i in range(start_index, len(array), interval):
        if i > len(array) + 1:
            break
        else: 
            res.append(array[i])
    return res

