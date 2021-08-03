def to_underscore(string):
    return ''.join('_' + c.lower() if c.isupper() else c for c in str(string)).lstrip('_')
