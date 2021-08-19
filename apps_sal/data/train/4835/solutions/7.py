def okkOokOo(s):
    s = s.lower().replace(',', '').replace(' ', '').replace('!', '?').replace('o', '0').replace('k', '1').split('?')
    res = ''
    for i in s[:-1]:
        res = res + chr(int(i, base=2))
    return res
