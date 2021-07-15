from collections import Counter 
def scramble(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s2 = list((Counter(s2) - Counter(s1)).elements())
    if len(s2) > 0:
        return False
    else:
        return True
