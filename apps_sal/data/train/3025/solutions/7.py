def locate(seq, value): 
    for x in seq:
        if x == value:
            return True
        if isinstance(x, list):
            if locate(x, value) == True:
                return True
    return False
