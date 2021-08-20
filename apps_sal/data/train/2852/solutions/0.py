def find_longest(st):
    (res, pos) = (0, [0])
    for (i, b) in enumerate(st, 1):
        if b == '(':
            pos.append(i)
        else:
            try:
                pos.pop()
                res = max(res, i - pos[-1])
            except:
                pos.append(i)
    return res
