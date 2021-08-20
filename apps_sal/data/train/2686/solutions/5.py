from string import ascii_lowercase as al
xs = ''.join((c.upper() if c in 'aeiou' else c for c in al)) * 2
tbl = str.maketrans(al + al.upper(), xs[1:] + xs[0])


def changer(s):
    return s.translate(tbl)
