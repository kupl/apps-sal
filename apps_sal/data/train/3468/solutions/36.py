def scramble(s1,s2):
    l=[]
    for x in s2:
        if x not in l:
            if s1.count(x)<s2.count(x):
                return False
            l.append(x)
    return True
