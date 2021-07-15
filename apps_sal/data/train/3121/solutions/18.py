def solve(arr):
    arr = set(arr)
    lst = list(map(abs,arr))
    one = 0
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            one = lst[i]

    if one in arr:
        return one
    else:
        a = "-"+str(one)
        return int(a)
