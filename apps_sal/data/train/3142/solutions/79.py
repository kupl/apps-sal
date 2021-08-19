def seven_ate9(str_):
    removals = []
    for i in range(len(str_) - 2):
        if str_[i] == '7' and str_[i + 1] == '9' and (str_[i + 2] == '7'):
            removals.append(i + 1)
    str_ = list(str_)
    for index in sorted(removals, reverse=True):
        del str_[index]
    return ''.join(str_)
