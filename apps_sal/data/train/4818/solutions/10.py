def solution(a, b):
    res = []
    if len(a) > len(b):
        res.append(b)
        res.append(a)
        res.append(b)
    else:
        res.append(a)
        res.append(b)
        res.append(a)
    return "".join(res)
