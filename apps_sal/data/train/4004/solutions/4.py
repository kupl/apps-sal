def first_dup(stg):
    return next((c for c in stg if stg.count(c) > 1), None)
