def decode(s):
    if type(s) != str:
        return 'Input is not a string'
    st = {}
    it = 0
    for i in 'abcdefghijklmnopqrstuvwxyz':
        st[i] = 'abcdefghijklmnopqrstuvwxyz'[::-1][it % 26]
        st[i.upper()] = st[i].upper()
        it += 1
    m = ''
    for im in s:
        if im.isalpha():
            try:
                m += st[im]
            except:
                pass
        else:
            m += im
    return m
