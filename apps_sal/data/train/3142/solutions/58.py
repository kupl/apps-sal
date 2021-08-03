def seven_ate9(str_):
    if '797' not in str_:
        return str_
    else:
        str_ = str_.replace('797', '77')
        return seven_ate9(str_)
