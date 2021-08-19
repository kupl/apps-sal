def locate(seq, v):
    return any((s for s in seq if s == v or (isinstance(s, list) and locate(s, v))))
