x=int(input())
for a in range(x):
 n=int(input())
 L=[str(n)]
 c=1
 while(len(L)!=n):
  L.append(str(n+c))
  if len(L)==n:
   break
  L.append(str(n-c))

  c+=1

 a=" ".join(L)

 print(a)

