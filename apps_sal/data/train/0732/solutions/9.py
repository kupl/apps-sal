try:
 for i in range(int(input())):
  n=int(input())
  ai=list(map(int,input().split()))
  bi=list(map(int,input().split()))
  sa=0
  sb=0
  ans=0
  if n==1:
   if ai[0] == bi[0]:
    print(ai[0])
   else:
    print(0)
  else :
   for i in range(0,n):
    if i==0 :
     if ai[i]==bi[i]:
      sa=sa+ai[i]
      sb=sb+bi[i]
      ans=ans+ai[i]
    elif sum(ai[:i]) == sum(bi[:i]) :
     if ai[i] == bi[i]:
      ans=ans+ai[i]
    else:
     sa=sa+ai[i]
     sb=sb+bi[i]
   print(ans)
except:
 pass
