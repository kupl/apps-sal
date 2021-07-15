for i in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 b=list(map(int,input().split()))
 c=[]
 for j in range(len(a)):
  c.append(a[j]*b[j])
 #print c.index(max(c))
 mx=max(c)
 ndx=[]
 temp=[]
 for j in range(len(c)):
  if c[j]==mx:
   ndx.append(j)
 for j in ndx:
  temp.append(b[j])
 print(b.index(max(temp))+1)

