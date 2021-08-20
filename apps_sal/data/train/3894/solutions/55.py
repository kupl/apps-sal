def solve(s):
    low_cnt = 0
    up_cnt = 0
    temp = list(s)
    for item in temp:
        if item.islower():
            low_cnt += 1
        else:
            up_cnt += 1
    if low_cnt >= up_cnt:
        return s.lower()
    else:
        return s.upper()
