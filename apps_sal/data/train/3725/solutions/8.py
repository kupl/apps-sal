def shift_left(a, b):
    return next((len(a) + len(b) - 2*len(b[i:]) for i in range(len(b)) if a.endswith(b[i:])), len(a) + len(b))
