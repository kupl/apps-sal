def seven_ate9(str_):
    out = str_[0]
    for i in range(1, len(str_) - 1):
        if str_[i] == '9' and str_[i - 1] == str_[i + 1] == '7':
            continue
        else:
            out += str_[i]
    return out + str_[-1]
