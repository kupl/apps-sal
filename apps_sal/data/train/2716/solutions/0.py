def encode(s, t=str.maketrans('aeiou', '12345')):
    return s.translate(t)


def decode(s, t=str.maketrans('12345', 'aeiou')):
    return s.translate(t)
