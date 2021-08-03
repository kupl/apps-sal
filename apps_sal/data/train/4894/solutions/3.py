def makeParts(arr, chunkSize):
    lst = []
    for i in range(0, len(arr), chunkSize):
        lst.append(arr[i:i + chunkSize])
    return lst
