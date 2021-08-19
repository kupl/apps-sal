def no_repeat(stg):
    return next((c for c in stg if stg.count(c) == 1))
