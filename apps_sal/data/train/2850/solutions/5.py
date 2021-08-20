def gordon(s):
    fmt = '{}!!!!'.format
    table = str.maketrans('AEIOU', '@****')
    return ' '.join((fmt(a.translate(table)) for a in s.upper().split()))
