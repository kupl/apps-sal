def has_subpattern(s):
    return False if (s + s).find(s, 1, -1) == -1 else True
