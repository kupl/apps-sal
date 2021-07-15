def rankings(arr):
    return [sum(j > i for j in arr)+1 for i in arr]

