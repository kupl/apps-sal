def string_to_number(s):
    res = 0
    neg = 1
    print(s)
    l = len(s) - 1
    for i in s:
        if i == '-':
            neg = -1
            l = l - 1
        else:
            res += int(i) * 10 ** l
            l = l - 1
        print(res)
    return res * neg
