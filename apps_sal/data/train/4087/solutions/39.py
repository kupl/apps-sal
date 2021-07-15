def get_char(c):
    '''
    Accepts decimal input
    returns extended ascii character representation of input
    '''
    return bytes.fromhex(hex(c)[2:]).decode(encoding="latin1")

