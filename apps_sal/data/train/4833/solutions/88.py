def replace_exclamation(s):
    for i in "AEUIOaeuio":
        s = s.replace(i,"!")
    return s
