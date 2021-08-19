def seven_ate9(s):
    while s.count('797') != 0:
        s = s.replace('797', '77')
    return s
