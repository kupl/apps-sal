def array(string=''):
    strings = string.split(',')
    return None if len(strings) < 3 else ' '.join([strings[i] for i in range(1, len(strings) - 1)])
