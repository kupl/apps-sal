import re


def sursurungal(txt):
    return re.sub('([0-9]+) ([a-z]+)', lambda x: change(x.group(1), x.group(2)), txt)


def change(n, w):
    n = int(n)
    if n <= 1:
        return str(n) + ' ' + w
    elif n == 2:
        return str(n) + ' bu' + w.rstrip('s')
    elif n > 2 and n <= 9:
        return str(n) + ' ' + w.rstrip('s') + 'zo'
    else:
        return str(n) + ' ' + 'ga' + w.rstrip('s') + 'ga'
