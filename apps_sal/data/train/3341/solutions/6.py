def pop_shift(stg):
    d, m = divmod(len(stg), 2)
    return [stg[:d+m-1:-1], stg[:d], stg[d] if m else ""]
