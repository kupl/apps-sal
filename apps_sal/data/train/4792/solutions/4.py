def parse_float(s):
    if type(s) == str and __import__('re').match(r'[\d\.]+', s):
        return float(s)
