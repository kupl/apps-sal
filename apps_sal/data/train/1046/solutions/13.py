t=int(input())
i=0
while i<t:
 a,b=input().split()
 a=int(a)
 b=int(b)
 ai=1
 ae=1
 bi=2
 be=2
 while True:
  if ae<=a:
   ai+=2
   ae+=ai
  else:
   print("Bob")
   break
  if be<=b:
   bi+=2
   be+=bi
  else:
   print("Limak")
   break
 i+=1
