def correct(string):
    inttab = '501'
    outtab = 'SOI'
    x = string.maketrans(inttab, outtab)
    return string.translate(x)
