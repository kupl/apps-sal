def charCheck(s, m, sp):
    s = s.replace([' ',''][sp],'')
    return [s[:m]==s,s[:m]]
