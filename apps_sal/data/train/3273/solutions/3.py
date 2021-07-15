from collections import Counter

def solve(str1, str2):
    C, S = Counter(str1), set(str2)
    return all(v == 1 or k in S for k,v in C.items()) + 1
