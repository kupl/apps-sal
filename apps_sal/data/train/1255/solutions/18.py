T=int(input())
for i in range(0,T):
 a,b=input().split()
 b=int(b)
 n=len(a)
 a=list(set(a))
 r=[]
 for c in range(97,123):
  if(len(r)==n):
   break
  else:
   if chr(c) not in a:
    r.append(chr(c))
   else:
    if(b>0):
     r.append(chr(c))
     b=b-1
 if(len(r)!=n):
  print("NOPE")
 else:
  print(''.join(r))

