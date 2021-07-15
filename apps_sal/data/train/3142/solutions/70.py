def seven_ate9(s):
    while s.find('797') != -1:
        s = s.replace('797', '77')
    return s
