def binRota(arr):
    return [y for x in arr for y in (x, x[::-1])[arr.index(x) % 2]]
