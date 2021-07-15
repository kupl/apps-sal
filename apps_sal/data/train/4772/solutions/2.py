def name_score(name):
    up = name.upper()
    return {name: sum(up.count(c) * v for k, v in alpha.items() for c in k)}
