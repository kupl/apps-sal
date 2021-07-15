# cook your dish here
a = int(input())
for i in range(a):
 b = list(map(int,str(input()).split(' ')))
 Ans = 0
 for i1 in range(b[2]+1):
  if (b[0]^i1)<(b[1]^i1):
   Ans+=1
 print(Ans)
