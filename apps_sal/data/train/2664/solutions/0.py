def solve(s):
    v = sum(s[i] != s[-1-i] for i in range((len(s))//2) )
    return v == 1 or not v and len(s)%2
