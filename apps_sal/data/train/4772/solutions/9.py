def name_score(name):
    score = 0
    for c in name:
        for k, v in alpha.items():
            if c.upper() in k:
                score += v
                break
    return {name:score}
