def seven_ate9(str_):
    new_strng = ''
    for (i, e) in enumerate(str_[:-1]):
        try:
            if e != '9':
                new_strng += e
            elif i == 0:
                new_strng += e
            elif str_[i - 1] != '7' or str_[i + 1] != '7':
                new_strng += e
        except IndexError:
            continue
    new_strng += str_[-1]
    return new_strng
