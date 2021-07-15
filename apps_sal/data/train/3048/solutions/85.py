def alternateCase(s):
    # your code here
    
    alternated = []
    
    for i in list(s):
        
        if i.isspace():
            alternated.append(i)
        
        if i.islower():
            alternated.append(i.upper())
        
        if i.isupper():
            alternated.append(i.lower())
    
    return  "".join(alternated)
