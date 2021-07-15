for _ in range(int(input())):
 m,n=map(int,input().split())
 l=[]
 for i in range(m):
  s=input()
  l.append(s)
 final=0
 for i in range(n):
  count=0
  for j in range(m):
   if l[j][i]=='1':
    count+=1
  if count>1:
   for k in range(count):
    final+=k
 print(final)
