r,c,n=list(map(int,input().split()))
a=set()

c2=[0 for i in range(r)]
d2=[0 for j in range(c)]

for i in range(n):
    c1,d1=list(map(int,input().split()))
    a.add((c1,d1))
    c2[c1]+=1 
    d2[d1]+=1 


mr=max(c2)
mc=max(d2)

p1=[]
p2=[]

for i in range(r):
    if c2[i]==mr:
        p1.append(i)

for j in range(c):
    if d2[j]==mc:
        p2.append(j)
        
ans=mr+mc 

for i in p1:
  for j in p2:
    if (i,j) in a:
      continue
    print(ans)
    return
ans -= 1
print(ans)

