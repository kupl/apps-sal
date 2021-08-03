def seven_ate9(str):
    while str.find('797') > -1:
        str = str.replace('797', '77')
    return str
