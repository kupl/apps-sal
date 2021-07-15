n=int(input())
k=[]
for i in range(n):
    l=input()
    k.append(l)
maxs=0
for j in range(7):
    s=0
    for i in range(n):
       if k[i][j]=='1':s+=1
    if s>maxs:maxs=s
print(maxs)

