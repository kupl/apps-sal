def solve(s,k):
    s = s.split()
    return sum(1 for i in range(len(s)) for j in range(len(s)) if i!=j and int(s[i]+s[j])%k==0)
