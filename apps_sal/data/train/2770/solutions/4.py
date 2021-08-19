def make_password(phrase):
    return ''.join((w[0] for w in phrase.split())).translate(str.maketrans('iIoOsS', '110055'))
