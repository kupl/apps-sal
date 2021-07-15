def replace_exclamation(s):
    vstr = "aeiouAEIOU"
    for x in s:
        if x in vstr:
            s = s.replace(x, "!")
    return s

