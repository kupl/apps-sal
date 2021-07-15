def capitalize(s):
    s_lower = "".join(s.lower() if i%2==0 else s.upper() for i,s in enumerate(s))
    s_upper = "".join(s.upper() if i%2==0 else s.lower() for i,s in enumerate(s))
    return [s_upper]+[s_lower]
