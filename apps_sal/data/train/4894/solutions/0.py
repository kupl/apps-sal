def makeParts(arr, csize):
    return [arr[i:i + csize] for i in range(0, len(arr), csize)]
