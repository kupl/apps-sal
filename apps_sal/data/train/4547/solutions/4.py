def more_zeros(stg):
    return sorted((c for c in set(stg) if f"{ord(c):b}".count("0") > 3), key=stg.index)
