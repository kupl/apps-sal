def replace_exclamation(s):
    v = "aeiouAEIOU"
    t = v.maketrans(v, "!" * len(v))
    return s.translate(t)
