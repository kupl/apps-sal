def swap(s):
    return s.translate(s.maketrans('aiueo', 'AIUEO'))
