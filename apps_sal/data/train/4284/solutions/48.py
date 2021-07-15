def array_leaders(numbers):
    res = []
    for pos, val in enumerate(numbers):
        if val > sum(numbers[pos+1::]):
            res.append(val)
    return res

