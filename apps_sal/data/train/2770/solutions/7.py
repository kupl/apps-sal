def make_password(phrase):
    return ''.join((i[0] for i in phrase.split())).translate(str.maketrans('sioSIO', '510510'))
