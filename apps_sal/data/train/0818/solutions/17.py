for _ in range(int(input())):
 n=int(input())
 m=[0]
 c=0
 l1=list(map(int,input().split()))
 for i in range(len(l1)):
  if(l1[i]%2==0):
   c+=1
  m.append(c)
 #print(m)
 for _ in range(int(input())):
  l,r=list(map(int,input().split()))
  s=m[r]-m[l-1]
  if(s==0):
   print("ODD")
  else:
   print("EVEN")

