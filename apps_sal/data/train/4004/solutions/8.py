def first_dup(s):
    if not s: return None
    for i in range(len(s)-1):
        if s[i] in s[i+1:]:
            return s[i]
    return None
