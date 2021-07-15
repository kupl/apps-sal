def array(string):
    array = string.split(',')[1:-1]
    new = ' '.join(array)
    return None if not new else new
