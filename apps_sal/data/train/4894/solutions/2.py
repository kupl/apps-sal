def makeParts(arr, chunkSize):
    r = list()
    while arr:
        r.append(arr[0:chunkSize])
        arr = arr[chunkSize:]
    return r
