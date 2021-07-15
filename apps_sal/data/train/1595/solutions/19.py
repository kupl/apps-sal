def bw(s):
    t=[]
    for i in s:
        if i=='b':
            t.append('0')
        else:
            t.append('1')
    return int(''.join(str(i) for i in t),2)
def pm(s):
    t=[]
    for i in s:
        if i=='-':
            t.append('0')
        else:
            t.append('1')
    return int(''.join(str(i) for i in t),2)
def inp(n):
    t=[]
    for i in range(n):
        s=input()
        t.append(pm(s))
    return t
def f(n,k,s):
    dp=[[0 for i in range(1024)] for i in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1024):
            dp[i][j]=dp[i-1][j]+dp[i-1][j^s[i-1]]
    return dp[n][k]
t=int(input())
for i in range(t):
    k=bw(input())
    n=int(input())
    print(f(n,k,inp(n)))
