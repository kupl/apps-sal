import re
def replace_dots(s):
    intab = '.'
    outtab = '-'
    trantab = str.maketrans(intab,outtab)
    return s.translate(trantab)
