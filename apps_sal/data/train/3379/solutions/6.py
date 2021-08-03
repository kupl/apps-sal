def encrypter(s, a=list(range(97, 123))): return s.translate(dict(zip(a[::-1], a[13:] + a[:13])))
