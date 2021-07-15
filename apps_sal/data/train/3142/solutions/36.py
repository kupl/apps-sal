def seven_ate9(s):
    s = s.replace('797', '77')
    if '797' in s:
        return seven_ate9(s)
    return s
