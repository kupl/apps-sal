def seven_ate9(str_):
    while str_.find('797') != -1:
        str_ = str_.replace('797', '77')
    return str_
