def vaporcode(s):
    vapor_s = ''.join(['{}  '.format(i) for i in s.upper().replace(' ','')])
    return vapor_s.rstrip()
