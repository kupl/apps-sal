def solve(s):
    res = []
    spaces = []
    cnt = 0
    for c in s:
        cnt += 1
        if c != ' ':
            res.insert(0, c)
        else:
            spaces.append(cnt)
    for pos in spaces:
        res.insert(pos-1, ' ')
    return ''.join(res)
