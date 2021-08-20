def remove(s):
    return ' '.join((r for (r, _) in __import__('re').findall('((!*)\\w+\\2)', s)))
