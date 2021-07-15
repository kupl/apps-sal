def every(array, interval = 1, start_index = 0):
    li = []
    for i in range(start_index,len(array),interval):
        li.append(array[i])
    return li

