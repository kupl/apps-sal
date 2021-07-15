def swap(s):
    return s.translate(s.maketrans('aeiou', 'AEIOU'))
