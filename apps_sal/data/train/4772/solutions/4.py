def name_score(name):
    score = sum((alpha[key] for key in alpha.keys() for x in name if x.upper() in key))
    return {name: score}
