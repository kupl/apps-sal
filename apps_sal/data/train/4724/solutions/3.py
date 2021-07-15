def drop_cap(stg):
    return " ".join(w.capitalize() if len(w) > 2 else w for w in stg.split(" "))
