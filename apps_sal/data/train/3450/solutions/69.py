def array(string):
    x = string.split(',')
    if len(x) < 3: return None
    return " ".join(x[1:-1])
