from collections import Counter as c
def scramble(s1, s2):
    s1 = c(s1)
    s2 = c(s2)
    for i in s2:
        if s1[i]<s2[i]:
            return False
    return True
