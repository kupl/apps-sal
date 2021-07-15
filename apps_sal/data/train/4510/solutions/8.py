def to_underscore(xs):
    return ''.join(('_' if i and x.isupper() else '') + x.lower() for i, x in enumerate(str(xs)))
