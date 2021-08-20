def min_value(digits):
    str_list = []
    stringulator = ''
    d_list = list(dict.fromkeys(digits))
    sorted_list = sorted(d_list)
    for s in sorted_list:
        stringulator += '{}'.format(s)
    result = int(stringulator)
    return result
