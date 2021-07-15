
b=[]
def bell(a):
 nonlocal b
 l=[[1]]
 if a==1: return 1
 b.append(1)
 if a==2: return 2
 b.append(2)
 l.append([1])
 l[1].append(2)
 for j in range(2,a):
  l.append([(l[j-1][j-1])%1000000007])
  for k in range(1,j+1):
   l[j].append((l[j][k-1]+l[j-1][k-1])%1000000007)
  b.append((l[j][j])%1000000007)
 return l[a-1][a-1]

n=eval(input())
bell(1000)
for i in range(0,n):
 x=eval(input())
 print(b[x-1])
