t=int(input())
for _ in range(t):
 s=input()
 l=[int(x) for x in s]
 ss=sum(l)
 if ss<5 and len(l)>1:
  print(9-ss)
 else:
  print(min(ss%9, 9-ss%9))


