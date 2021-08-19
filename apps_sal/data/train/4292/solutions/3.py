def string_clean(s):
    return __import__('re').sub('\\d', '', s)
