t = str.maketrans('gdrplkGDRPLKaeyouiAEYOUI', 'aeyouiAEYOUIgdrplkGDRPLK')
encode = decode = lambda s: s.translate(t)
