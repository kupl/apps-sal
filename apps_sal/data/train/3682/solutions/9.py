def string_constructing(a, s):
    if not s:
        return 0
    if set(s)-set(a):
        return False

    n = 1
    i = 0
    for c in s:
        while True:
            if i==len(a):
                i = 0
                n += 1
            if a[i]!=c:
                n += 1
                i+=1
            else:
                i+=1
                break
            
            
    return n+len(a)-i

