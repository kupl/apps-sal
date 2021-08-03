def split_without_loss(s, split_p):
    sep = split_p.replace("|", "")
    s1 = s.replace(sep, split_p)
    s1 = s1.strip("|")
    return s1.split("|")
