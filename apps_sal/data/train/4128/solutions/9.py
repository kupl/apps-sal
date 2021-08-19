def bears(n, s):
    return (lambda a: [''.join(a), n <= len(a)])(__import__('re').findall('B8|8B', s))
