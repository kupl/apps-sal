def remove_exclamation_marks(s):
    c = s.count("!")
    s = list(s)
    for i in range(c):
        s.remove("!")
    return "".join(s)
