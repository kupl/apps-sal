def every(array, interval=1, start_index=0):
    arr = []
    counter = 0

    for i in range(start_index, len(array)):
        if counter == interval:
            arr.append(array[i])
            counter = 0
        elif i == start_index:
            arr.append(array[start_index])
        counter += 1

    return arr
