def per(n, s=0):
    return ([n] if s else []) + (per(eval('*'.join(str(n))), 1) if n > 9 else [])
