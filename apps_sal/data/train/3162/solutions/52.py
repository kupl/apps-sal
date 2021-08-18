def compare(s1, s2):
    if s1 == None or not s1.isalpha():
        s11 = ""
    else:
        s11 = s1.upper()
    if s2 == None or not s2.isalpha():
        s12 = ""
    else:
        s12 = s2.upper()
    return sum(ord(s11[i]) for i in range(len(s11))) == sum(ord(s12[i]) for i in range(len(s12)))
