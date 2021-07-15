def locate(seq, value): 
    for s in seq:
        if s == value or (isinstance(s,list) and locate(s, value)): 
            return True
    return False
