def okkOokOo(s):
    s = s.lower()
    s = s.replace('o', '0')
    s = s.replace('k', '1')
    s = s.replace(',', '')
    s = s.replace(' ', '')
    s = s.replace('!', '')

    bis = s.split('?')
    for i in xrange(len(bis)):
        bis[i] = chr(int(bis[i], 2))

    return ''.join(bis)
