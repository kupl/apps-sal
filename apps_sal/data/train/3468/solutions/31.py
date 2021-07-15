from collections import Counter
def scramble(s1, s2):
    return True if len(Counter(s2)-Counter(s1))==0 else False
