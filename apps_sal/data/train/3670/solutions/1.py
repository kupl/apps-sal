def domino_reaction(s):
    return s.replace("|", "/", min(len(s.split(" ")[0]), len(s.split("/")[0])))
