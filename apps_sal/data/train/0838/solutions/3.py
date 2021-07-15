T = int(input())
for i in range(T):
 x = int(input())
 l= [int(x) for x in input().split()]
 t=[]
 for i in range(len(l)):
  t.append(l[i]+i) 
 print(max(t))

