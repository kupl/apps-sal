def seven_ate9(str_):
    i = 0
    length = len(str_)

    while i < length - 1:
        if str_[i] == '9' and str_[i - 1] == '7' and str_[i + 1] == '7':
            str_ = str_[:i] + str_[i + 1:]
            length -= 1
        i += 1
    return str_
