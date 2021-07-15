for _ in range(int(input())):
 n=int(input())
 s=list(input())
 if s.count('H')==s.count('T'):
  l=[]
  i=0
  while i<n:
   if s[i]!='.':
    l.append(s[i])
   i=i+1
  c=0
  for i in range(len(l)//2):
   if l[2*i]=="H" and l[(2*i)+1]=="T":
    c+=2
  if c==len(l):
   print("Valid")
  else:
   print("Invalid")
 else:
  print("Invalid")
