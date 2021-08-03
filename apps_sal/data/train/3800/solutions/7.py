import re


def spreadsheet(s):
    m = re.match(r'([A-Z]+)(\d+)$', s)
    if m:
        c, r = m.group(1), int(m.group(2))
        column = 0
        for d in c:
            column = column * 26 + (ord(d) - ord('A') + 1)
        return 'R{}C{}'.format(r, column)
    else:
        m = re.match(r'R(\d+)C(\d+)$', s)
        r, c = m.group(1), int(m.group(2))
        column = ''
        while(c > 0):
            m = c % 26
            if m == 0:
                m = 26
            column = chr(ord('A') + m - 1) + column
            c = (c - m) // 26
        return column + r
