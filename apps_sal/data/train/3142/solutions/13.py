def seven_ate9(str_):
    if '797' in str_:
        return seven_ate9(str_.replace('797', '77'))
    else:
        return str_
