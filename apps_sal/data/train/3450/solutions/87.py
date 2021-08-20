def array(string):
    return ' '.join(string.split(',')[1:-1]) if string and len(string.split(',')[1:-1]) > 0 else None
