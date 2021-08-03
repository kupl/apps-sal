def array(string):
    string = string.split(',')

    list = ' '.join(string[1:-1])

    if len(list) > 0:
        return list
    else:
        None
