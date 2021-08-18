
def added_char(s1, s2):
    s2 = list(s2)
    [s2.remove(i) for i in s1]
    return s2[0]
