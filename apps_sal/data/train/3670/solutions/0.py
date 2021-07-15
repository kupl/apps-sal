def domino_reaction(s):
    ds = ""
    for (i,d) in enumerate(s):
        if( d=="|" ): 
            ds += "/"
        else:
            return ds+s[i:]
    return ds

