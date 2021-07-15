try:
 t,m=input().split()
 t=int(t)
 m=list(m)
 letters=list("abcdefghijklmnopqrstuvwxyz")
 trans={}
 for i in range(len(letters)):
  trans[letters[i]]=m[i]
 for i in range(t):
  x=list(input())
  y=""
  for j in x:
   if(j.isalpha()==True):
    if(j.isupper()==True):
     y+=trans[j.lower()].upper()
    else:
     y+=trans[j]
   else:
    if(j=='_'):
     y+=" "
    else:
     y+=j
  print(y)
  
except:pass
