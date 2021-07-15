def drop_cap(str_):
    return " ".join(s.capitalize() if len(s) > 2 else s for s in str_.split(" "))
