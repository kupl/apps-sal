
for t in range(int(input())):
  
  n=int(input())
  a=list(map(int,input().split()))
  a.sort(reverse=True)
  b=c=0
  for i in a:
   if(b<c):
     b+=i
   else:
     c+=i
  print(max(b,c))
