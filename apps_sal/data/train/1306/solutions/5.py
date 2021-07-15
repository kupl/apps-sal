# cook your dish here
for i in range(int(input())):
 s = input()
 n = len(s)
 L,T,M,I,E=0,0,0,0,0
 for i in range(n):
  if s[i]=="L":
   L=L+1
  elif s[i]=="T":
   T=T+1
  elif s[i]=="I":
   I=I+1
  elif s[i]=="M":
   M=M+1
  elif s[i]=="E":
   E=E+1
 if L>1 and T>1 and I>1 and M>1 and E>1:
  print("YES")
 elif L==2 and T==2 and I==2 and M==2 and (E==1 or E==2):
  print("YES")
 elif n==5 and L==1 and T==1 and I==1 and M==1 and E==1:
  print("YES")
 else:
  print("NO")
