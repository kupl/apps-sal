def seven_ate9(str_):
    while True:
        if '797' in str_:
            str_ = str_.replace('797', '77', 1)
        else:
            return str_
