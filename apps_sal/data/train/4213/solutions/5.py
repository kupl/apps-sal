def array_info(arr):
    res = [len(arr), 0, 0, 0, 0]
    for i in arr:
        if type(i) == int:
            res[1] += 1
        elif type(i) == float:
            res[2] += 1
        elif type(i) == str:
            if len(i) * ' ' == i:
                res[4] += 1
            else:
                res[3] += 1
    return [[i] if i else [None] for i in res] if arr else 'Nothing in the array!'
