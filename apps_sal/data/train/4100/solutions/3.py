def reverse_alternate(string):
    res = []
    arr = string.split()
    for i in arr:
        if arr.index(i) % 2 == 1:
            res.append(arr[arr.index(i)][::-1])
        else:
            res.append(arr[arr.index(i)])
    return " ".join(res)
