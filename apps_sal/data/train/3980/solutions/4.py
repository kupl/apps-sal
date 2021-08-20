def reverse(s):
    return __import__('re').sub('(.)\\1+', lambda x: x.group(0).swapcase(), s)
