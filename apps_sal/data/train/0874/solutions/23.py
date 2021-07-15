for _ in range(int(input())):
 n,m,s=[int(x) for x in input().split()]
 h=list(map(int,input().split()))
 h.sort()
 sum=0
 count =0
 for i in h:
  if i<=s*2:
   count+=1
   if i<=s:
    m-=1
   else:
    m-=2
   if m==0:
    break
   elif m==-1:
    count-=1
    break
 print(count)

