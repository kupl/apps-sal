for text in range(int(input())):
 n,u,d=map(int,input().split())
 l=list(map(int,input().split()))
 a=1
 b=True
 for i in range(n-1):
  if l[i]<l[i+1] and (l[i]+u)>=l[i+1]:
   continue
  elif l[i]>l[i+1] and l[i]<=(l[i+1]+d):
   continue
  elif l[i]==l[i+1]:
   continue
  elif a==1 and l[i]>l[i+1]:
   a-=1
   continue
  else:
   b=False
   break
 if b==False:
  print(i+1)
 else:
  print(n)
