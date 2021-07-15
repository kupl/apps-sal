def compare(s1,s2):
    if s1=="" or s2=="":
        return True         
    elif s1.isalpha() and s2.isalpha():
        return sum([ord(c.upper()) for c in list(s1)]) == sum([ord(d.upper()) for d in list(s2)])
    elif s1.isalpha() == s2.isalpha():    
        return True
    else:
        return False
