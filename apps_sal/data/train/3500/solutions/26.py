def remove_exclamation_marks(s):
    s = list(s)
    for i in range(len(s)): 
        if "!" in s: 
            s.remove("!")
    return "".join(s)
