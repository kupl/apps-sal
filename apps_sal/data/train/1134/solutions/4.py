loop = int(input())
for iiiiiiiii in range(loop):
 no_sol = 0
 n,m= input().split()
 m=int(m)
 n = int(n)
 l = input().split()
 for nation in range(len(l)):
  l[nation] = int(l[nation])
 for i in range(len(l)):
  if i < m:
   no_sol += l[i]
  else:
   no_sol-=(l[i]/2)
   if no_sol<0:
    print("DEFEAT")
    break

 if no_sol>=0:
  print("VICTORY")

