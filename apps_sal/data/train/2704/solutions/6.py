def almost_increasing_sequence(s):
    p=-1
    l=len(s)
    for i in range(l-1):
        if s[i]>=s[i+1]:
            if p>=0: return False
            p=i
    return p<=0 or p==l-2 or s[p-1]<=s[p+1]
