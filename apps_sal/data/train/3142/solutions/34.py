def seven_ate9(str_):
    res = list(str_)
    for i in range(len(str_)):
        if str_[i:i+3] == '797':
            res[i+1] = ''
    return "".join(res)

