e=10**9+7
n=100000
l=[1]
for i in range(1,n+1):
    x=(i*(2*i-1))%e
    l.append((x*l[-1])%e)
t=int(input())
for _ in range(t):
    n=int(input())
    print(l[n])

