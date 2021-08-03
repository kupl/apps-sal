def makeParts(arr, size):
    return [arr[i:i + size] for i in range(0, len(arr), size)]
