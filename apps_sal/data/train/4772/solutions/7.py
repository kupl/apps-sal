def name_score(name):

    def score(x):
        return sum((alpha[a] if x in a else 0 for a in alpha))
    return {name: sum((score(n) for n in name.upper()))}
