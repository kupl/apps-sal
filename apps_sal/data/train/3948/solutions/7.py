def sel_reverse(arr,l):
    if not l:
        return arr
    arr = [sorted(arr[i: i + l])[::-1] for i in range(0, len(arr), l) ]
    return [j for i in arr for j in i]
