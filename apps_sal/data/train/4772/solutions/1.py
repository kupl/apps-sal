def name_score(name):
    return {name: sum(alpha[key] for c in name for key in alpha if c.upper() in key)}
