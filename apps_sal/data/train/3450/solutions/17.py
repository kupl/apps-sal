def array(string):
    str_list = string.split(',')
    if len(str_list) < 3:
        return None
    str_list.pop(0)
    str_list.pop(len(str_list) - 1)
    return ' '.join(str_list) if str_list != '' else None
