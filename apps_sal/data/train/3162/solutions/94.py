def compare(s1, s2):
    if s1 == None or not s1.isalpha():
        s1_scr = 0
    else:
        s1_scr = sum((ord(i) for i in s1.upper()))
    if s2 == None or not s2.isalpha():
        s2_scr = 0
    else:
        s2_scr = sum((ord(i) for i in s2.upper()))
    return s1_scr == s2_scr
