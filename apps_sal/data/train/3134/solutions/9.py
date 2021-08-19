def is_valid(idn):
    return __import__('re').match('^[a-zA-Z_\\$][a-zA-Z0-9_\\$]*$', idn) is not None
