def stringy(size):
    st = ''
    while size > 0:
        st += '1'
        size -= 1
        if size < 1:
            break
        st += '0'
        size -= 1
    return st
