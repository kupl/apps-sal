def gimme(arr):
    for (i, el) in enumerate(arr):
        if el != min(arr) and el != max(arr):
            return i
