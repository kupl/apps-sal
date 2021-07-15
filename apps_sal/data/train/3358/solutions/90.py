def correct(s):
    x = s.maketrans('501','SOI')
    return s.translate(x)
