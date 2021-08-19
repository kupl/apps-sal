def replace_dashes_as_one(s):
    return __import__('re').sub('-( *-)+', '-', s)
