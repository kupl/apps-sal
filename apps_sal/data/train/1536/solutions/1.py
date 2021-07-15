from statistics import mode
t=int(input())
for _ in range(t):
 n=int(input())
 l=list(map(int,input().split()))
 ll=len(l)
 diff=list()
 if(ll==4):
  diff.append(((l[3]-l[0])//3))
 for i in range(ll-1):
  diff.append(l[i+1]-l[i])
 x=mode(diff)
 if(l[0]-l[1]!=x and l[2]-l[1]==x):
  l[0]=l[1]-x
 for i in range(ll-1):
  if(l[i+1]-l[i]!=x):
   l[i+1]=l[i]+x
   
 for i in range(ll):
  print(l[i],end=" ")
 print()
