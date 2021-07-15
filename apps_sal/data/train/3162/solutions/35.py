def compare(s1, s2):
    val_s1, val_s2 = 0 if s1 == None or not s1.isalpha() else sum(map(ord, s1.upper())), 0 if s2 == None or not s2.isalpha() else sum(map(ord, s2.upper()))
    return val_s1 == val_s2
