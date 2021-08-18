'''
n=int(input())
a=list(map(int,input().split()))
def lastcount(r):
    nonlocal a
    right=a[r]
    left=a[r-1]
    i=r
    j=r-1
    k=0
    while j>=0:
        k+=left==right
        j-=2
        i-=1
        left=left^a[i]^a[j]^a[j+1]
        right=right^a[i]
    return k
dp=0
for i in range(n-1,0,-1):
    dp+=lastcount(i)
print(dp)
'''
n = int(input())
a = list(map(int, input().split()))
o = {}
e = {}
t = a[0]
e[t] = 1
o[0] = 1
ans, i = 0, 1
odd = True
while i < n:
    t ^= a[i]
    if odd:
        ans += o.get(t, 0)
        o[t] = o.get(t, 0) + 1
    else:
        ans += e.get(t, 0)
        e[t] = e.get(t, 0) + 1
    i += 1
    odd = 1 - odd
print(ans)
