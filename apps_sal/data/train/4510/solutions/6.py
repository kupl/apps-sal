def to_underscore(s):
    if isinstance(s, (int, float)):
        return str(s)
    
    return ''.join([c if c == c.lower() else "_"+c.lower() for c in s ]).strip("_")
