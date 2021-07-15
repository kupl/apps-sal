def debug(s):
    return __import__('re').sub(r'bug(?!s)', '', s)
