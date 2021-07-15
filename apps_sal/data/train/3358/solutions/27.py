def correct(string):
    replace = {'5':'S', '0':'O', '1':'I'}
    for key, value in list(replace.items()):
        string = string.replace(key, value)
    return string

