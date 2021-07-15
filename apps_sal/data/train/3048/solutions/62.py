def alternateCase(s):
    n_s=''
    if s.isspace():
        return s
    for i in s:
        if i.isupper():
            n_s+=i.lower()
        elif i.lower():
            n_s+=i.upper()
        else:
            n_s+=i
    return n_s            
