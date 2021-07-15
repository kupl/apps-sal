def diff(arr):
    r = [abs(int(w.split('-')[0])-int(w.split('-')[1])) for w in arr]
    return arr[r.index(max(r))] if sum(r) else False
