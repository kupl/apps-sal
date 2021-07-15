for _ in range(int(input())):
 n=int(input())
 aux=[0]*n
 tot=0
 for i in range(n):
  s=list(map(int,list(input())))
  aux[i]=sum(s[:n//2])-sum(s[n//2:])
 tot=sum(aux)
 if tot==0:
  print(0)
 else:
  x=[]
  for i in range(len(aux)):
   x.append(abs(tot-(2*aux[i])))
  print(min(x))
