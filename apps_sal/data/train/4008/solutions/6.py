def string_to_int_list(string):
    return [int(i) for i in string.split(',') if i.isdigit() or (i.startswith('-') and i[1:].isdigit())]
