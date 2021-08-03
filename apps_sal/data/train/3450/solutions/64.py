def array(string):
    return ' '.join(list(string.split(','))[1:-1]) if len(list(string.split(','))) > 2 else None
