def makeParts(arr, chunkSize):
    store = []
    while len(arr) >= chunkSize:
        store.append(arr[:chunkSize])
        arr = arr[chunkSize:]
    if len(arr) > 0:
        store.append(arr)
    return store
