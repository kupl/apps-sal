def seven_ate9(str_):
    if '797' not in str_:
        return str_
    else:
        return seven_ate9(str_.replace('797', '77'))
