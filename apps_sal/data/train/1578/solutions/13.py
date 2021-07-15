def int_(s):
 try: 
  int(s)
  return True
 except ValueError:
  return False
t=int(input())
while t>0:
 c = str(input())
 s=0
 for i in c:
  if int_(i):
   s=s+int(i)
 print(s) 
 t=t-1
