def to_underscore(s):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in str(s)]).strip('_')
