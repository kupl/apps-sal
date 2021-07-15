def vaporcode(s):
    string = ''
    s = ''.join(s.split()).upper()
    for c in s:
        string += c + '  '
    return string[:-2]
