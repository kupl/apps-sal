def domino_reaction(s):
    i = next((i for i,j in enumerate(s) if j in "/ "),len(s))
    return "/"*i+s[i:]
