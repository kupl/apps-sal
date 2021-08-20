def make_password(phrase, mapping=dict(['i1', 'o0', 's5'])):
    return ''.join((mapping.get(c.lower(), c) for (c, *rest) in phrase.split()))
