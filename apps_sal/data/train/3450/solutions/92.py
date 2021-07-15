def array(string):
    result = string.replace(',', ' ').split()
    return None if len(result) < 3 else ' '.join(result[1:-1])
