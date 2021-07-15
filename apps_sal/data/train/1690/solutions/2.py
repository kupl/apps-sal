def check_relative(i,j):
    if is_relative[i] or i==j:return
    if len(land[i].intersection(land[j]))>=k:
        is_relative[i]=True
        for ii in range(n):
            check_relative(ii,i)

n,k=map(int,input().split())
land=[]
is_relative=[False]*n
for i in range(n):
    p,*q=input().split()
    land.append(set(q))

for i in range(n):
    check_relative(i,0)
        
print(is_relative.count(True))
