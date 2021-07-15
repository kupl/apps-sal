tc=int(input())
z=[]
for i in range(tc):
 n, m, x, y = [int(x) for x in input().split()]
 n1 = n - 1
 n2 = n - 2
 m1 = m - 1
 m2 = m - 2

 if n1%x==0 and m1%y==0:
   z.append("Chefirnemo")
 elif n2%x==0 and m2%y==0:
  if n2>=0 and m2>=0:
   z.append("Chefirnemo")
  else:
   z.append("Pofik")
 else:

   z.append("Pofik")

for i in range(tc):
 print(z[i])
