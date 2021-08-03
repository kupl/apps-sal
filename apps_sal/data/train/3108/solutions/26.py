def multi_table(number):
    str = ""
    for i in range(10):
        str = str + "{} * {} = {}\n".format(i + 1, number, (i + 1) * number)
    str = str[0:-1]
    return str
