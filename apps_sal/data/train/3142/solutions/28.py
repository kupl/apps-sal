def seven_ate9(str_):
    x = str_.replace('797', '77')
    while str_ != x:
        str_ = x
        x = str_.replace('797', '77')
    return str_
