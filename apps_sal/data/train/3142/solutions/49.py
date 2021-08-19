def seven_ate9(str_):
    s = str_
    while '797' in s:
        s = s.replace('797', '77')
    return s
