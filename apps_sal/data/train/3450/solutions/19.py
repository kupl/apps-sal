def array(string):
    str_slice = string.split(',')[1:-1]
    return ' '.join(str_slice) if str_slice else None
