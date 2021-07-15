def find_longest(arr):
    print(len(str(arr[0])))
    res = []
    for i in arr:
        res.append(len(str(i)))
    return arr[res.index(sorted(res,reverse=True)[0])]
