def compare(s1,s2):
    
    if s1 is None or s1.isalpha() is False:
        s1 = ""
    if s2 is None or s2.isalpha() is False:
        s2 = ""
    
    return True if sum([ord(x) for x in s1.upper()]) == sum([ord(x) for x in s2.upper()]) else False
