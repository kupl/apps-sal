def gimme(arr):
    list = [i for i in arr if i != max(arr) and i != min(arr)]
    return arr.index(list[0])
