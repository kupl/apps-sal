def alphabetic(s):
    n = len(s)
    c = [s[i] for i in range(len(s))]
    c.sort(reverse=False)
    for i in range(n):
        if (c[i] != s[i]):
            return False
        
    return True
