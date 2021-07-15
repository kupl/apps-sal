def array(string):
    k = ' '.join(string.split(',')[1:-1])
    if k: return k
    else: return None
