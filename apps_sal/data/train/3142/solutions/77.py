def seven_ate9(sInput):
    lst = list(sInput)
    res = ''
    for i in range(len(lst) - 1):
        if not(i and lst[i] == '9' and lst[i - 1] == '7' and lst[i + 1] == '7'):
            res += lst[i]

    res += lst[len(lst) - 1]
    return res
