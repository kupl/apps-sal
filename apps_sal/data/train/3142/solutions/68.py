def seven_ate9(str_):
    res = ''
    for i, x in enumerate(str_):
        if x != '9' or i == 0 or i == len(str_) - 1:
            res += f'{x}'
        else:
            if str_[i - 1] != '7' or str_[i + 1] != '7':
                res += f'{x}'
    return res
