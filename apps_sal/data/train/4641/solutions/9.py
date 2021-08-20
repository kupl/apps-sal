def unique_in_order(it):
    return [it[0]] + [e for (i, e) in enumerate(it[1:]) if it[i] != e] if it else []
