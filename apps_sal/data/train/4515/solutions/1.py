def diff(arr):
    r = [abs(eval(s)) for s in arr]
    return arr[r.index(max(r))] if r and max(r) else False

