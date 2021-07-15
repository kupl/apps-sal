for i in range(eval(input())):
 a=list(map(int,input().split()))
 a.sort()
 b=set(a)
 k=eval(input())
 count=len(b)
 if count==1:
  ans=1+3*(k-1)
  print(ans)
 if count==2:
  if k<=a[0]+1:
   ans=1+3*(k-1)
   print(ans)
  else:
   ans=a[0]+a[1]+a[2]-1-((a[2]-k)*2)
   print(ans)
 if count==3:
  if k<=a[0]+1:
   ans=1+3*(k-1)
   print(ans)
  elif k<=a[1]+1:
   ans=1+3*(a[0])+2*(k-(a[0]+1))
   print(ans)
  else:
   ans=k+a[0]+a[1]
   print(ans)



