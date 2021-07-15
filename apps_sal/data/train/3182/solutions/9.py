def is_enough(lst):
    return len(lst) >= 10

def LDTA(n):
    res = []
    for i in range(1, 20):
        c = str(n ** i)
        for digit in c:
            if digit not in res:
                res.append(digit)
            if is_enough(res): break
        if is_enough(res): break
    if is_enough(res):
        return int(res[-1])
    return
