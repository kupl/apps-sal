def seven_ate9(str_):
    s = str_.replace('797', '77')
    return seven_ate9(s) if s != str_ else str_
