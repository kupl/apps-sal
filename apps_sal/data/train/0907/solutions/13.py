t=int(input())
for i in range(t):
 s=[]
 b=[]
 c=0
 n=int(input())
 s=input()
 for j in s:
  if(j!="."):
   b.append(j)
 if(len(b)==0):
  print("Valid")
 elif(len(b)%2!=0):
  print("Invalid")
 elif(b[0]!='H' or b[-1]!='T'):
  print("Invalid")
 else:
  for j in range(len(b)-2):
   if(b[j]!=b[j+2]):
    c=1
    break
  if(c==0):
   print("Valid")
  else:
   print("Invalid")

