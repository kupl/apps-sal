def solve(arr):
    for (i, el) in enumerate(arr):
        if arr.count(el * -1) == 0:
            return el
