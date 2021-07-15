for k in range(int(input())):
 n,k=list(map(int,input().split()))
 l=list(map(str,input().split()))
 while k>0:
  if l[-1]=="T":
   l.pop()
  else:
   for i in range(0,len(l)-1):
    if l[i]=="H":
     l[i]="T"
    else:
     l[i]="H"
   l.pop()
 
  k=k-1
 print(l.count("H"))
 
 

