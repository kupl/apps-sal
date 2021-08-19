def first_non_repeating_letter(s):
    seen = set()
    rep = set()
    for c in s:
        c = c.lower()
        if c in seen:
            rep.add(c)
        else:
            seen.add(c)
    for c in s:
        if c.lower() not in rep:
            return c
    return ''
