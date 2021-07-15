M=int(input())
ls=[]
ans=[]
k=2
for i in range(M):
    ls.append(int(input()))
for i in range(max(ls)):
    titu=ls[0]%k
    tmp=list(filter(lambda x:(x%k) == titu,ls))
    if len(tmp)==len(ls):
        ans.append(k)
    k+=1

for i in ans:
    print(i,end=" ")

