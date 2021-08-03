def counting_valleys(s):
    res, cnt = 0, 0
    for i in s:
        cnt += {'F': 0, 'U': 1, 'D': -1}[i]
        if cnt == 0 and i == 'U':
            res += 1

    return res
