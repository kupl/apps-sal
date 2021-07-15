def seven_ate9(str_):
    s_pattern = "797"
    r_pattern = "77"
    while s_pattern in str_:
        str_ = str_.replace(s_pattern, r_pattern)
    return str_
