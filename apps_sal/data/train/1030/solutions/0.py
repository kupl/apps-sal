t = int(input())
while(t>0):
 t-=1;
 n,l,r = list(map(int,input().split()));
 a = bin(l)[2:];
 b = bin(r)[2:];
 # find matching
 z = 0;
 l = min(len(a),len(b));
 for i in range(l):
  if a[i]==b[i]:
   z+=1;
  else:
   break;

 #find base string
 a = a[z:]
 b = b[z:]
 if(len(a)==0 and len(b)==0):
  print(n);
 else :
  m = max(len(a),len(b))
  #print m;
  zz = bin(n)[2:]
  x= len(zz)
  y = zz[:x-m]
  
  f1 = y+a;
  f2 = y+b;
  ans = int(y,2)
  if(int(f1,2)>n or int(f2,2)>n):
   ans-=1;
  
  print(ans) 
  

  

