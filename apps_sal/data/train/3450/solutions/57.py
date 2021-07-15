def array(s):
    if len(s.split(',')) < 3:
        return
    else:
        return ' '.join(s.split(',')[1:-1])
