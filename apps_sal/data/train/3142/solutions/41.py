def seven_ate9(str_):
    res = list(str_)
    for i in range(len(str_)-2, 0, -1):
        if res[i] == '9' and res[i+1] == res[i-1] == '7':
            res.pop(i)
    return ''.join(res)
