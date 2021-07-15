# cook your dish here
for _ in range(int(input())):
 n=int(input())
 l=input()
 k="T"
 h=t=0
 f=0
 for i in range(n):
  if(l[i]=="H"):
   if(k=="T"):
    h+=1
    k="H"
   else:
    print("Invalid")
    f=1
    break
  elif(l[i]=="T"):
   if(k=="H"):
    t+=1
    k="T"
   else:
    print("Invalid")
    f=1
    break
 if(f==0):
  if(h!=t):
   print("Invalid")
  else:
   print("Valid")

