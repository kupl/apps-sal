def array(string):
    new = string.split(',')
    if string == '' or len(new) <= 2:
        return None
    else:
        new = new[1:len(new) - 1]
        new_str = ' '.join(new)
        return new_str
