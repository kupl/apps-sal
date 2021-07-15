def alternateCase(s):
    
    string = ""
    
    for i in s:
        if i.isupper():
            i = i.lower()
            string += i
        else:
            i = i.upper()
            string += i
            
    return string
