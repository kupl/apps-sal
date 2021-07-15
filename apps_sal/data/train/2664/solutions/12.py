def solve(s):    
    c=sum(s[i]!=s[-1-i] for i in range(len(s)//2))
    return c==1 or (c==0)*len(s)%2

