def correct(s):
    st = ''
    for c in s:
        if c == '5':
            st += 'S'
        elif c == '0':
            st += 'O'
        elif c == '1':
            st += 'I'
        else:
            st += c
    return st
