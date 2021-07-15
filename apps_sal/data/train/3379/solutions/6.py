encrypter=lambda s,a=list(range(97,123)):s.translate(dict(zip(a[::-1],a[13:]+a[:13])))
