def array(string):
    new_string = string.split(',')[1:-1]
    if len(new_string) == 0:
        return None
    else:
        return ' '.join(new_string)
