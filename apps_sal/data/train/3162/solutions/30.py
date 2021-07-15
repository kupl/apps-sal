def compare(s1,s2):
    if s1 == None or s2 == None:
        return True
    if not s1.isalpha():
        s1 = ""
    if not s2.isalpha():
        s2 = ""
    s1 = s1.upper()
    s2 = s2.upper()
    return sum([ord(el) for el in s1]) == sum([ord(el) for el in s2])
