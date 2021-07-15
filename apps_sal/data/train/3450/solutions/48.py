def array(string):
    s1 = string.split(",")
    s2 = str(" ".join(s1[1:-1]))
    return s2 if s2 else None
