def string_clean(s):
    deprecated = '0123456789'
    return ''.join([s_ for s_ in s if s_ not in deprecated])
