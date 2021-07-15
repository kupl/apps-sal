t=int(input())
for i in range(t):
 n=input()
 co=0
 m=n[0]
 for j in range(1,len(n)):
  if m!=n[j]:
   co+=1
   m=n[j]
  if co>2:
   print("non-uniform")
   break
 if co<=2:
  print("uniform")
