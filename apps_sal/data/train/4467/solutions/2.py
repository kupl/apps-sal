
def remember(str_):
    return [c for i,c in enumerate(str_) if str_[:i].count(c) == 1]
