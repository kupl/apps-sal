for _ in range(int(input())):
 n=int(input())
 s=list(map(int,input().split()))
 maxx=0
 count=0
 if n<=2:
  print(n)
 elif n==3:
  if s[2]==s[1]+s[0]:
   print(3)
  else:
   print(2)
 else:
  for i in range(2,n):
   if s[i]==s[i-1]+s[i-2]:
    count+=1
    maxx=max(maxx,count)
   else:
    count=0
  print(maxx+2)
  
  


