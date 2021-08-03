def spreadsheet(s):
    try:
        r, c = map(int, s[1:].split('C'))
        l = str(r)
        while c:
            c, i = divmod(c - 1, 26)
            l = chr(i + 65) + l
        return l
    except:
        c = 0
        for i, l in enumerate(s):
            if l.isdigit():
                break
            c = 26 * c + ord(l) - 64
        return 'R%sC%d' % (s[i:], c)
