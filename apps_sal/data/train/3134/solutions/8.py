def is_valid(idn):
    return bool(__import__('re').match('^[a-zA-Z_$][\\w$]*$', idn))
