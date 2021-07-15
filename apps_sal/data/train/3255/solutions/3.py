def only_duplicates(stg):
    return "".join(c for c in stg if stg.count(c) > 1)
