def binRota(arr):
    arr[1::2] = map(lambda x: x[::-1], arr[1::2])
    return sum(arr,[])
