def array(string):
    string = string.split(',')
    if len(string) <= 2:
        return None
    else:
        string.pop(0)
        string.pop(len(string) - 1)
    return ' '.join(string)
