# cook your dish here
ans = []
mxlen = 0

def lcs(a,b,d,mxlen):
    L = [0]*(n+1)
    for i in range(n+1):
        L[i] = [0]*(n+1)
    #print("#",L,a,b)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    #print(L)
    if L[n][n] > mxlen:
        mxlen = L[n][n]
        i,j = n,n
        t = []
        while i>0 and j>0:
            if a[i-1] == b[j-1]:
                t.insert(0,a[i-1])
                i -= 1
                j -= 1
            elif L[i-1][j] > L[i][j-1]:
                i -= 1
            else:
                j -= 1
        #print(t)
        ans.append({d:t})

try:
    n = int(input())
    a = [int(w) for w in input().split()]
    b = [int(w) for w in input().split()]
    minb = min(b)
    b = [(i-minb-1) for i in b]
    for i in range(-1000,1001):
        bb = b.copy()
        bb = [(j+i) for j in bb]
        lcs(a,bb,i,mxlen)
    ans = sorted(ans, key=lambda i: len(list(i.values())[0]),reverse = True)
    t = ans[0]
    d = list(t.keys())[0]
    t = t[d]
    print(len(t))
    print(*t)
    t = [(i-d+minb+1) for i in t]
    print(*t)
except:
    pass
