def domino_reaction(s):
    p = s.find(' ')
    q = s.find('/')
    r = p if q==-1 else q if p==-1 else min(p,q)
    return s.replace('|','/',r)
