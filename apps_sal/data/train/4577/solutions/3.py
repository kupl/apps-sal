def debug(s):
    return __import__('re').sub('bug(?!s)', '', s)
