def array(string):
    print(string)
    return ' '.join(string.split(',')[1:-1]) if len(string.split(',')) > 2 else None
