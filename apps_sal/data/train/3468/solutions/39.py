from collections import Counter

def scramble(s1,s2):
    a = Counter(s1)
    b = Counter(s2)
    a.subtract(b)
    new = []
    for i in a:
        if a[i] >= 0:
            new.append(i)
    return len(new) == len(a)




