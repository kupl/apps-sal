def seven_ate9(s):
    if '797' in s:
        return seven_ate9(s.replace('797', '77'))
    return s
