def is_keith_number(n):
    res = [int(x) for x in str(n)]
    tmp = sum(res)
    cnt = 1
    while tmp < n:
        cnt += 1
        res.pop(0)
        res.append(tmp)
        tmp = sum(res)
        if tmp == n:
            return cnt
    return False
