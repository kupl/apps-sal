from math import gcd
for _ in range(int(input())):
    n,a,k,min_k,e = int(input()),[int(i) for i in input().split()],0,0,-1   
    for j in range(n):
     if(a[j] != -1):break            
    for i in range(j,n):
     if min_k==0:min_k,e = a[i],a[i]+1 
     else:
      if min_k < a[i]:min_k = a[i]                
      if(a[i] == -1):pass
      else:
       if(a[i] == e):pass
       else:
        if( k == 0):k = e-a[i]
        else:
         new_k = e-a[i]
         if(new_k < 0):k = -1
         else:k = gcd(k,new_k)
        if(k<min_k or k<0): k = -1; break
      if k != 0 and a[i]!=-1: e = a[i]%k+1
      else:e += 1             
    if(k == -1):print("impossible")
    elif k == 0 :print("inf")
    else:print(k)  
