def divide(weight):
    res = []
    for i in range(2, weight + 1):
        if i % 2 == 0:
            res.append(i)
    if res[-1] == weight:
        res.pop(-1)
    n = 0
    while n < len(res):
        if res == []:
            return False
        elif res[0 + n] + res[-1 - n] == weight:
            return True
        else:
            n += 1
    return False
