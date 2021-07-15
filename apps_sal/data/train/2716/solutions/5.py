def cipher(mode):
    table = str.maketrans(*['aeiou', '12345'][::mode])
    return lambda s: s.translate(table)

encode, decode = cipher(1), cipher(-1)
