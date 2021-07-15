def name_score(name):
    scores = {k: v for keys, v in alpha.iteritems() for k in keys}
    return {name: sum(scores.get(a, 0) for a in name.upper())}
