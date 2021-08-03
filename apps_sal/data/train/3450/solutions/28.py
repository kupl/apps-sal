def array(string):
    lst = string.split(',')
    if len(lst) < 3:
        return None
    lst.pop(0)
    lst.pop(-1)
    return ' '.join(lst)
