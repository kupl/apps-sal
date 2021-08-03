ALPHA = {c: v for s, v in alpha.items() for c in s}


def name_score(name):
    return {name: sum(ALPHA.get(c, 0) for c in name.upper())}
