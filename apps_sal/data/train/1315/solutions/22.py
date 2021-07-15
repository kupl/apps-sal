n=int(input())
ar = [sorted(list(map(int,input().split()))) for i in range(n)]
c=0
for j in range(n):
    if ar.count(ar[j])==1:
        c+=1
    else:
        pass
print(c)
