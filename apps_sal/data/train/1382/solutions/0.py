n=int(input())
a=list(map(int,input().split()))
x=int(input())
l=[]
for i in a:
 if i<0:
  l.append(-i)
l.sort()
m=len(l)
ans=0
if l:
 if x>n:
  ans=sum(l)
 else:
  ans=sum(l[m-x:])
print(ans)

 

