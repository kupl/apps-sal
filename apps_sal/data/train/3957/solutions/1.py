

def uniq_c(s):
    lst = []
    c = 1
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            lst.append((s[i],c))
            c = 1
        else:
            c += 1
    if s:
        lst.append((s[-1],c))
    return lst
