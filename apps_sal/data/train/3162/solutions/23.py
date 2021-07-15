def compare(s1,s2):
    if s1 is None or not s1.isalpha():    s1=""
    if s2 is None or not s2.isalpha():    s2=""
    if sum([ord(x) for x in s1.upper()])==sum([ord(x) for x in s2.upper()]):    return True
    else:    return False
