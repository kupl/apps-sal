for t in range(int(input())):
 a,b=map(int, input().split())
 for i in range(1,501,2):
  a-=i
  if a<0:
   print("Bob")
   break
  b-=(i+1)
  if b<0:
   print("Limak")
   break
