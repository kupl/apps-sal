def array(str):
    l = len(str) > 2
    a = str.replace(' ', '').strip(',')
    b = a.split(',')
    c = b[1:-1]
    return ' '.join(c) if str and l and a and b and c else None
