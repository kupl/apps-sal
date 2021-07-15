import array
T = int(input())
for _ in range(T):
 N,M = list(map(int,input().split()))
 robots = array.array('I')
 robots.extend((0,)*((N>>5)+1))
 c = 0
 Id = M
 while robots[Id>>5] & (1 << (Id&31))==0:
  robots[Id>>5]+=1<<(Id&31)
  c+=1
  Id = (Id+M)%N
 if c==N:
  print("Yes")
 else:
  print("No",c)
