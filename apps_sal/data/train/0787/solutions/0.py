for _ in range(int(input())):
 l=list(map(int,input().strip()))
 for j in range(len(l)-1,-1,-1):
  if l[j]==1:
   l.pop()
  else:
   break
 if l.count(1):
  time,prev,z,c=0,0,0,0
  for j in range(len(l)-1,-1,-1):
   if l[j]==0:
    z+=1
    continue
   if prev!=z:
    prev=z
    c+=1
   time+=c+z

  print(time)
 else:
  print(0)


