def seven_ate9(str_):
    res = str_[0]
    for i in range(1, len(str_) - 1):
        if str_[i - 1] == '7' and str_[i + 1] == '7' and str_[i] == '9':
            continue
        else:
            res += str_[i]
    return res + str_[-1]
