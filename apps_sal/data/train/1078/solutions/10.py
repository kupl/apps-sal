for _ in range(int(input())):
 a = list(map(int,input().split()))
 s = a.pop(0)
 sm = sum(a)
 ans = 0


 while sm>0:
  a1 = a[::-1]
  s1, i = 0, 0
  while s1<s and i<len(a):
   s1+=a[i]
   i+=1
  if s1>s:
   i-=1
   s1-=a[i]
  s2, i1 = 0, 0
  while s2<s and i1<len(a):
   s2+=a1[i1]
   i1+=1
  if s2>s:
   i1-=1
   s2-=a[i1]
  # print(sm, s1, s2, a, i, i1, ans)
  if i1>i:
   sm-=s2
   a = a1[i1:][::-1]
  else:
   sm-=s1
   a = a[i:]
  ans+=1
 print(ans)




