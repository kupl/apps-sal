from collections import Counter
def pr(a):return (a*(a-1))//2
n,p,k=list(map(int,input().split()))
a=list(map(int,input().split()))
a=Counter([(x**4-x*k+p)%p for x in a])
print(sum(pr(a[x]) for x in a))

