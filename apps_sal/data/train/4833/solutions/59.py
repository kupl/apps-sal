def replace_exclamation(s):
    ss = ""
    for el in s:
        if el not in "euioaEUIOA":
            ss += el
        else:
            ss += "!"
    return ss
