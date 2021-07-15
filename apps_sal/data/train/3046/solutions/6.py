def thue_morse(n):
    '''Returns the n first digits of the Thue-Morse sequence.'''
    code = '0'
    while len(code) < n:
        code += code.translate(code.maketrans('01','10'))
    return code[:n]
