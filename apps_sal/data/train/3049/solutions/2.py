def textin(s):
    return __import__('re').sub('(?i)t[wo]?o', '2', s)
