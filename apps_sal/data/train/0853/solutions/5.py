t = int(input())
for _ in range(t):
 n = int(input())
 l = 2*n
 l1 = []
 l2 = []
 for i in range(l):
  if i%2 == 0:
   s = input()
   #x = input()
   l1.append(s)
  else:
   s = int(input())
   l2.append(s)
 #print(l2)
 t1 = []
 t1 = sorted(l2)
 
 t2 = []
 #print(t1)
 for i in t1:
  #print(l2.index(i))
  t2.append(l1[l2.index(i)])
 for j in t2:    
  print(j)
