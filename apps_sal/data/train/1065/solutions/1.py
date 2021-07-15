for a in range(int(input())):
    N,M=map(int,input().split())
    b=[]
    for o in range(N):
     b.append(input())
    c=[]
    for d in b:
     f=[]
     for e in range(len(d)):
      if d[e]=='1':
       f.append(e)
     c.append(f)
    i=[]
    for g in range(len(c)):
     for h in range(len(c[g])):
      for j in range(len(c)):
       for k in range(len(c[j])):
        if (j>g) or(j==g and k>h):
         if c[g][h]-c[j][k]>=0:
          i.append(c[g][h]-c[j][k]+j-g)
         else:
          i.append(-1*(c[g][h]-c[j][k])+j-g)
    l=[m for m in range(1,N+M-1)]
    for n in l:
     print(i.count(n),end=' ')
  
