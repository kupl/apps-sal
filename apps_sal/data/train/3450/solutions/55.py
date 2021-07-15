def array(string):
    string_list = string.split(',')
    return ' '.join(string_list[1:-1]) if string_list[1:-1] else None

