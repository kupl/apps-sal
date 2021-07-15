def name_score(name):
    score = lambda x: sum(alpha[a] if x in a else 0 for a in alpha)
    return {name : sum(score(n) for n in name.upper())}
