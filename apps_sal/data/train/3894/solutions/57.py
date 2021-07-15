def solve(s):
    l = sum(map(lambda x: x.islower(), s))
    u = len(s) - l
    
    if l >= u:
        return(s.lower())
    else:
        return(s.upper())
