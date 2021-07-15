def domino_reaction(s):
    return s.replace("|", "/", min([s.find(d) if s.find(d)!=-1 else len(s)  for d in " /"]) )

