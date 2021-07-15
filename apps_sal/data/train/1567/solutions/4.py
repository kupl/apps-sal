# cook your dish here
for _ in range(int(input())):
 n=int(input())
 s=list(input())
 d=dict()
 for i in s:
  d[i]=d.get(i,0)+1
 # print(d.values())
 if (n//2)%2==0:
  for i in list(d.values()):
   if i%2==1:
    print("NO")
    break
  else:
   print("YES")
 else:
  c=0
  for i in list(d.values()):
   if i%2==1:
    c+=1
    if c==3:
     print("NO")
     break
  else:
   print("YES")
   

