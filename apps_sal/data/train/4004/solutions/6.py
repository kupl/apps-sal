def first_dup(s):
    for i, v in enumerate(s):
        if v in s[i + 1:]:
            return v
