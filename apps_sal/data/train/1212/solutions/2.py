t = int(input())
S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while t > 0:
 max=1000000
 s=input()
 d={}
 ll=[]
 for str in S:
  d[str]=0
 for i in range(1,27):
  if len(s) % i==0:
   ll.append(i)
 for i in s:
  d[i]+=1
 l=sorted(d.items(), key=lambda ele: ele[1], reverse=True)
 i=0; ans=0
 while i < len(ll):
  cnt=len(s) // ll[i]
  for j in range(ll[i]):
   if l[j][1] < cnt:
    ans+=cnt-l[j][1]
  i+=1
  if ans < max:
   max=ans
  ans=0
 print(max)
 t -= 1
