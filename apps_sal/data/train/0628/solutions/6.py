t=int(input())
for _ in range(t):
 l=list(input())
 # for i  in l:
 #     print(i)
 ind=l.index('W')
 x=len(l)-1-ind
 res=x^ind
 if res==0:
  print("Chef")
 else:
  print("Aleksa")

