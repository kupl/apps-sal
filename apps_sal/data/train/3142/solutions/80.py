def seven_ate9(str_):
    return ''.join(('' if str_[i] == '9' and str_[i - 1] == '7' and (str_[i + 1] == '7') else str_[i] for i in range(len(str_) - 1))) + str_[-1]
