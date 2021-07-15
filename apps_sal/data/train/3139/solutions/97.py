def index(array, n):
    arr = []
    for i in array:
        arr.append(pow(i, n))
    if n > len(arr) - 1:
        return -1
    return arr[n]
