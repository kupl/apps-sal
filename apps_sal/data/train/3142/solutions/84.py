def seven_ate9(str_):
    while '797' in str_:
        i9 = str_.find('797')
        str_ = str_[:i9 + 1] + str_[i9 + 2:]
    return str_
