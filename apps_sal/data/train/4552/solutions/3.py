def rankings(arr):
    return[sorted(arr)[::-1].index(v)+1 for v in arr]
