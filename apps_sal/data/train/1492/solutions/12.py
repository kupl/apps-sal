def lcs(A,B):
 a,b=len(A),len(B)
 lst=[[None]*(b+1) for _ in range(a+1)]
 for x in range(a+1):
  for y in range(b+1):
   if x==0 or y==0:
    lst[x][y]=0
   elif A[x-1] == B[y-1]:
    lst[x][y]= 1+lst[x-1][y-1]
   else:
    lst[x][y]=max(lst[x][y-1],lst[x-1][y])
 return lst[a][b]

for _ in range(int(input())):
 n=int(input())
 lst=[]
 for i in range(n):
  stg=input()
  axx=list(set(stg))
  if axx == ['a'] or axx == ['b']:
   lst.append(0)
   continue
  m=len(stg)
  cnta=stg.count('a')
  cntb=stg.count('b')
  if cnta>cntb:
   lst.append(lcs(stg,m*'b'))
  elif cntb>cnta:
   lst.append(lcs(stg,m*'a'))
  else:
   lst.append(min(lcs(stg,m*'a'),lcs(stg,m*'b')))
 print(min(lst))

