def group(arr):
    lst = [[i] * arr.count(i) for i in arr]
    re = []
    for n in lst:
        if n not in re:
            re.append(n)
    return re
