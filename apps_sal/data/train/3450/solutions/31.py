def array(string):
    if len(string.split(',')) < 3:
        return
    return ' '.join(string.split(',')[1: -1])
