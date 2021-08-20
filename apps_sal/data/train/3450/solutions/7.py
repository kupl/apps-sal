def array(string):
    split = string.split(',')
    remove = split[1:-1]
    return ' '.join(remove) if remove else None
