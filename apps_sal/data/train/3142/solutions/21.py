def seven_ate9(str_):
    str_ = list(str_)
    for i in range(len(str_) - 1):
        if str_[i] == '9':
            if str_[i - 1] == str_[i + 1] == '7':
                str_[i] = ''
    return ''.join(str_)
