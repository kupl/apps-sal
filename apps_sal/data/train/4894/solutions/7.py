from math import ceil
def makeParts(arr, c): return [arr[i * c:i * c + c] for i in range(ceil(len(arr) / c))]
