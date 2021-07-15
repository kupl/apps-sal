def nerdify(txt):
    intab = 'aelAE'
    outab = '43143'
    trantab = str.maketrans(intab,outab)
    return txt.translate(trantab)
