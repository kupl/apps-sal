def distinct(seq):
    res = []
    for num in seq:
        if num not in res:
            res.append(num) 
    print(res)
    return res

