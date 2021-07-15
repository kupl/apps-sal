def remember(stg):
    return [c for i, c in enumerate(stg) if stg[:i].count(c) == 1]
