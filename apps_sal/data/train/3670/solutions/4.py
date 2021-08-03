def domino_reaction(stg):
    return stg.replace("|", "/", len(stg) - len(stg.lstrip("|")))
