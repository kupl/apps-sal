n=int(input())
a=[sorted(list(map(int,input().split()))) for i in range(n)];c=0
for j in range(n):
    if a.count(a[j])==1:
        c=c+1
print(c)
