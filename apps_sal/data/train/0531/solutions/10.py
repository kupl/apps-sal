n=int(input())
l=[]
for _ in range(n):
 a,h=map(int,input().split())
 l.append([a,h])
ans=2
if n==1:
 ans=1
 print(ans)
 return
l[0].append("left")
l[n-1].append("right")
for i in range(1,n-1):
 if l[i-1][2]=="right":
  if abs(l[i][0]-(l[i-1][1]+l[i-1][0]))>l[i][1]:
   ans+=1
   l[i].append("left")
  elif abs(l[i][0]-l[i+1][0])>l[i][1]:
   ans+=1
   l[i].append("right")
  else:
   l[i].append("stand")
 else:
  if abs(l[i][0]-l[i-1][0])>l[i][1]:
   ans+=1
   l[i].append("left")
  elif abs(l[i][0]-l[i+1][0])>l[i][1]:
   ans+=1
   l[i].append("right")
  else:
   l[i].append("stand")
print(ans)
