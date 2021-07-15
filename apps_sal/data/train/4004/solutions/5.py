def first_dup(s):
    if s[0] in s[1:]:
        return s[0]
    return len(s)>1 and first_dup(s[1:]) or None
