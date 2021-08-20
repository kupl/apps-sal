def seven_ate9(str_):
    counter = 0
    while counter <= str_.count('797'):
        str_ = str_.replace('797', '77')
        counter += 1
    return str_
