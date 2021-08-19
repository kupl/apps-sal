def name_score(name):
    return {name: sum((alpha[k] for c in name.upper() for k in alpha if c in k))}
