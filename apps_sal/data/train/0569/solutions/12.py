for n in range(int(input())):
 x=int(input())
 v=x+1
 j=-1+int((8*v)**.5)
 j//=2
 d=j*(j+1)//2
 if d==v:
  print(j-1)
 else:
  print(v-d-1)

