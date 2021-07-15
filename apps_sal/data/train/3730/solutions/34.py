def capitalize(s): 
    abc = ''.join([k.capitalize() for k in[s[i-2:i] for i in range(2,len(s)+2,2)]]) 
    return [abc,''.join([a.upper() if a == a.lower() else a.lower() for a in list(abc)])]

