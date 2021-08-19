def repeating_fractions(n, d):
    (a, b, c) = str(n * 1.0 / d).partition('.')
    return a + b + __import__('re').sub('(.)\\1+', lambda x: '(%s)' % x.group(1), c)
