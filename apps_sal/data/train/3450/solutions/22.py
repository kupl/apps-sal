def array(string):
    list = string.split(',')[1:-1]
    if len(list) == 0:
        return None
    else:
        return ' '.join(list)
