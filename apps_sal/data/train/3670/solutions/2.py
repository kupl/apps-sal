def domino_reaction(s):
    return (len(s) - len(s.lstrip('|'))) * '/' + s.lstrip('|')
