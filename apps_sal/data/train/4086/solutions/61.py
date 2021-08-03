def first_non_consecutive(arr):
    d = [arr[0]]
    for i in arr:
        d.append(i + 1)
    if len(list(set(d[:-1]).difference(arr))) == 0:
        return None
    else:
        return min(list(set(d[:-1]).difference(arr))) + 1
