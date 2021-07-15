def domino_reaction(s):
    i = next((i for i,c in enumerate(s) if c != '|'), len(s))
    return '/'*i + s[i:]
