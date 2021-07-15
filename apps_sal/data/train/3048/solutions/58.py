def alternateCase(s):
    S=""
    for i in s:
        if i.isupper():
            S+=i.lower()
        else:
            S+=i.upper()
        
    return S
