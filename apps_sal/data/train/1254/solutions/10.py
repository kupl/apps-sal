T=int(input())
for i in range(T):
 N,P=list(map(int,input().split()))
 S=list(map(int,input().split()))[:N]
 c=0
 d=0
 for j in range(len(S)):
  if S[j]>=P//2:
   c+=1
  elif S[j]<=P//10:
   d+=1
 if c==1 and d==2:
  print("yes")
 else:
  print("no")

