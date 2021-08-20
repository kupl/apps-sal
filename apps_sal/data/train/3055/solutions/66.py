def sum_str(a, b):
    if len(str(a + b)) == 0:
        return '0'
    try:
        a = int(a)
    except:
        return str(b)
    try:
        b = int(b)
    except:
        return str(a)
    return str(a + b)
